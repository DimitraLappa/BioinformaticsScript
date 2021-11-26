#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a simple scipt for addressing the problem presented in the Technical Interview

MIT License

Copyright (c) 2021, BioinformaticsScript, Dimitra Lappa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Futures
from __future__ import print_function
from __future__ import unicode_literals

# Built-in/Generic Imports
import os
import sys
import io

# Libs
import pandas as pd 
from collections import Counter
import smtplib
from email.mime.text import MIMEText




__author__ = 'Dimitra Lappa'
__copyright__ = 'Copyright 2021, Bioinformatics Interview Question'
__credits__ = ['Dimitra Lappa']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Dimitra Lappa'
__email__ = 'demilappa@gmail.com'
__status__ = 'Dev'


##################################################################################################
def unique(list1):
	#Function to get unique values
	#Print directly by using * symbol
	print(*Counter(list1))
	return Counter(list1)


def identify_origins(filename):
	#Function that identifies unique origins for each file 
	df=pd.read_csv(filename)

	#Getting sample IDs and identifying sample origins
	sampleIDs = df['sample']
	sample_origins = []
	for sampleID in range(len(sampleIDs)):
		ID=str(sampleIDs[sampleID])
		sample_origins.append(ID[1])				
	return sample_origins


def identify_failed_samples(filename,origins,unique_sample_origins):
	#Function for identifying the failed samples for each origin source
	df=pd.read_csv(filename)
	df['origin_source'] = origins
	source_failure_perc = []

	#Identify failed sample for each origin source and print respective message
	for origin in unique_sample_origins:
		print("For the origin source: ",origin)
		subset_origin_source = df[df['origin_source'] == origin]	# Subset each source samples' from the origincal file 
		subset_fail = subset_origin_source[(subset_origin_source['pct_covered_bases']<95)|(subset_origin_source['qc_pass']==False)]	# Subset the samples that failed
		fails = subset_fail.shape
		fails_perc = (fails[0]*100)/unique_sample_origins[origin]	# Calculate the failure percentage
		print("The number of failed samples is ",fails[0],"out of ",unique_sample_origins[origin],"total samples, hence the percentage of failed samples is: ",(fails_perc),"%")
		source_failure_perc.append( fails_perc)
	return(source_failure_perc)


def send_email(source_fail, filename):
	#Notify user if there is a failed sample origin
	if any(fail_perc > 10 for fail_perc in source_fail):
		
		#Open log file with the results	and append them to email
		results_file = open(filename, 'r')
		results_message = results_file.read()
 		results_file.close()

		#Request destination email and user password
		emailUser = raw_input("Excessive percentage of failed samples detected, please provide an email adress: ")
		print("A warning email, with a summary of the test results will be send to: ",emailUser)
		password = raw_input("Please provide your password: ")	
	
		warning = str('Warning:the latest batch of samples analysed, contains multiple failed samples')
		message = results_message+warning
		try:
			#Sending email process
			smtp = smtplib.SMTP('smtp.gmail.com', 587)
			smtp.starttls()	#Use TLS to add security 
			smtp.login("demilappa@gmail.com",password)
			smtp.sendmail("demilappa@gmail.com",emailUser,str(message)) 
			smtp.quit() 
   			print ("Warning email was sent successfully") 	
		except Exception as ex: 
	    		print("Unfortunately, something went wrong and the warning email was not sent.",ex)
	return(emailUser)		


def main():
	print("Reading the files in the current working directory")
	current_dir = os. getcwd()
	for filename in os.listdir(current_dir):
		if filename.endswith(".txt"):
			
			#Redirecting the results in an output log file
			original_stdout = sys.stdout
			with open('Results','w') as log:
				sys.stdout = log
				print(os.path.join(current_dir, filename))
				print("This is a new samples' file")

				#Isolating the sources of samples and calculating failure percentage
				print("The origins of the samples,for this file, are: ")
				origin_sources = identify_origins(filename)
				sample_origins_for_input = unique(origin_sources)
				failed_samples_percentage = identify_failed_samples(filename, origin_sources,sample_origins_for_input)

				#Redirecting to original stdoutput	
				sys.stdout = original_stdout
			mail = send_email(failed_samples_percentage,'Results')
			continue


if __name__ == "__main__":
	main()
