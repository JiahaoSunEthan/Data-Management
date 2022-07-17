# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:53:39 2021

@author: 13451
"""



from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName('readfile')\
    .getOrCreate()

import pyspark.sql.functions as fc
country = spark.read.json('country.json') 
country.groupBy('Continent').agg(fc.avg("LifeExpectancy").alias("avg_le"),fc.count("*").alias("cnt")).filter('cnt>=20').orderBy(fc.desc('cnt')).limit(1).select('Continent','avg_le').show()
