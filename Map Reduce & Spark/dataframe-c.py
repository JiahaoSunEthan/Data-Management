# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:44:12 2021

@author: 13451
"""

from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName('readfile')\
    .getOrCreate()

country = spark.read.json('country.json') 
country[['Continent']].distinct().show()
