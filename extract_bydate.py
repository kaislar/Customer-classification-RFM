#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 23:05:11 2017

@author: kais
"""
#prend en argument la date sup des transactions à considérer
 
import csv
import math
import sys 
from datetime import datetime
import os

data_file = "./reduced.csv"
path_output="/media/kais/Kais/datasetRNN/"
interest_date= sys.argv[1]
print str(interest_date) 
date_format = "%Y-%m-%d"
a = datetime.strptime(interest_date, date_format)
client=0
c = csv.writer(open(path_output+interest_date+".csv", "wb"))
c.writerow(["customer","order_date","grand_total","order_id"])
i=0

for e, line in enumerate( open(data_file) ):
	if (e==0): 
		continue
	
	else :	
		# si la date de la ligne est dans la marge 
		# print line.split(",")[10] 
		delta= a - datetime.strptime(line.split(",")[6], date_format)
		if ( delta.days > 0 ) : 
			i+=1
			if ( i % 1000000 == 0 ) : 
				print str(i) 
			#print line.split(",")[6]
			#c.writerow([line.split(",")[0],line.split(",")[6],line.split(",")[10],line.split(",")[1]])
			c.writerow([line.split(",")[0],line.split(",")[6],line.split(",")[10],","])
			

		
	
