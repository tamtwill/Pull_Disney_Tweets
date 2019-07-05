#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 20:03:22 2019

@author: tam
"""
import csv
import os
import wget

picpathC = [insert path to California photos]
picpathF = [insert path to Florida photos]  
filenameC = insert path to California data]   
filenameF = [insert path to Florida data] 
 
def getPics(picpath, filename):
    with open(filename) as csvfile:
        csvrows = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csvrows:
            url = row[0]
            print(url)
            wget.download(url, out=picpath)


getPics(picpathC, filenameC)
os.remove(filenameC)
    
getPics(picpathF, filenameF)
os.remove(filenameF)