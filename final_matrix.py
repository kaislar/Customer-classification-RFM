#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 10:07:01 2017

@author: kais
"""
import csv
import numpy 
import matplotlib.pyplot as plt
import math
import pandas

###########################################################################
#Generation du fichier contenant la base de donnée en format t , t +1 ,.. t+n
###########################################################################
def creation_liste():
	import os
	from datetime import datetime, timedelta
	delta=timedelta(days=30)

	date_format = "%Y-%m-%d"
	date_max_str='2013-07-28'
	date_min_str='2012-03-02'
	date_max=datetime.strptime(date_max_str, date_format)
	date_min=datetime.strptime(date_min_str, date_format)

	l=[]
	i=date_min
	while(i<date_max): 
		l.append(str(i)[:10])
		i+=delta  
	return l 


if __name__=='__main__' : 
    file_path= '/media/kais/Kais/datasetRNN/RFM/'
    path_output="/media/kais/Kais/datasetRNN/RFM"
    liste_fichiers= creation_liste()
    file_name="2012-04-01_RFM.csv"
    dataframe = pandas.read_csv( file_path+file_name ,engine= 'python' , skipfooter=3)
    dataset =dataframe.values
    dataset = dataset.astype( 'float32' )		
    liste_clients= dataframe["customer"].values
    df = pandas.DataFrame({'R0': dataframe["recency"].values, 'F0': dataframe["frequency"].values, 'M0': dataframe["monetary_value"].values},   index = liste_clients)
    k=0
    
    df=df.ix[:,['F0','R0','M0']]

    for j in liste_fichiers[2:]  :
        k+=1
        file_name= j+"_RFM.csv"
        dataframe = pandas.read_csv( file_path+file_name ,engine= 'python' , skipfooter=3)
        liste_clients_int=dataframe["customer"].values
        dataset = dataset.astype( 'float32' )	
        dataframe = pandas.DataFrame({'R0': dataframe["recency"].values, 'F0': dataframe["frequency"].values, 'M0': dataframe["monetary_value"].values},   index = liste_clients_int)
    
        print  df.loc[liste_clients]
        df['F'+str(k)]=pandas.Series(dataframe.loc[liste_clients,'F0'], index = liste_clients)
        df['R'+str(k)]=pandas.Series(dataframe.loc[liste_clients,'R0'], index = liste_clients)
        df['M'+str(k)]=pandas.Series(dataframe.loc[liste_clients,'M0'], index = liste_clients)
    dataframe2 = pandas.read_csv( file_path+"categories.csv" ,engine= 'python' , skipfooter=3)
    liste_clients_int=dataframe2["customer"].values
    dataframe2 = pandas.DataFrame({'R_Quartile': dataframe2["R_Quartile"].values, 'F_Quartile': dataframe2["F_Quartile"].values, 'M_Quartile': dataframe2["M_Quartile"].values, 'RFMClass': dataframe2["RFMClass"].values},   index = liste_clients_int)
    df['Fcat']=pandas.Series(dataframe2.loc[liste_clients,'F_Quartile'], index = liste_clients)
 
  
    df['Rcat']=pandas.Series(dataframe2.loc[liste_clients,'R_Quartile'], index = liste_clients)
    df['Mcat']=pandas.Series(dataframe2.loc[liste_clients,'M_Quartile'], index = liste_clients)
    df['RFMClass']=pandas.Series(dataframe2.loc[liste_clients,'RFMClass'], index = liste_clients)
  
    liste_categories=df["RFMClass"].values
    liste_categories= set(liste_categories)
    print liste_categories
    df.to_csv(file_path+'dataset_seq.csv')
