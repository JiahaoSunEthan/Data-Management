# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:27:08 2021

@author: 13451
"""



from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName('readfile')\
    .getOrCreate()

country = spark.read.json('country.json') 
country[country.Continent == 'North America'][['Name']].show(truncate=False)