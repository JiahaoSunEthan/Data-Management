# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 21:30:45 2021

@author: 13451
"""

from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName('readfile')\
    .getOrCreate()

country = spark.read.json('country.json') 
city = spark.read.json('city.json') 
country.join(city, country.Capital== city.ID).select(country['Name'],city['Name']).show(truncate=False)