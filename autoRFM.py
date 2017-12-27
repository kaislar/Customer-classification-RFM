#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 11:05:14 2017

@author: kais
"""

import os
from datetime import datetime, timedelta
#Dans ce script on pourrait utiliser une liste de clients provenant d'un fichier quelquonque pas nécessairement le premier 
#Les clients non existant dans les fichiers des tj précédents auront RFM=0 
#ce qui signifie pour le réseau récurrent une absence d'information 

path_input= '/media/kais/Kais/datasetRNN/'
path_output='/media/kais/Kais/datasetRNN/RFM/classification/'
delta=timedelta(days=30)
date_format = "%Y-%m-%d"
# max et min de la dataset
date_max_str='2013-07-28'
date_min_str='2012-03-02'
date_max=datetime.strptime(date_max_str, date_format)
date_min=datetime.strptime(date_min_str, date_format)
#liste de clients à considerer
l=[]
i=date_min
while(i<date_max): 
	l.append(str(i)[:10])
	i+=delta  
print l 

k=0
for i in l :
	if (k==0) : 
		#k=1
		continue
	else :  
		#os.system("python rfm.py -i " + str(i)+".csv -o ./RFM/"+ str(i)+"_RFM.csv -d "+str(i))
		print  "python rfm.py -i "+ path_input + str(i)+".csv -o "+path_output+ str(i)+"_RFM.csv -d "+str(i)	
		os.system("python rfm-analysis.py -i "+ path_input + str(i)+".csv -o "+path_output+ str(i)+"_RFM.csv -d "+str(i))
	
		#RFM-analysis.py -i <orders.csv> -o <rfm-table.csv> -d <yyyy-mm-dd>'
