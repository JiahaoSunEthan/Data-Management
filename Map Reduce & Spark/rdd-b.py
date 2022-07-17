# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 15:13:19 2021

@author: 13451
"""

from pyspark.sql import SparkSession
spark = SparkSession\
    .builder\
    .appName('readfile')\
    .getOrCreate()

country = spark.read.json('country.json')
city = spark.read.json('city.json')
country_rdd = country.rdd.map(lambda r:(r['Capital'],r['Name']))
city_rdd = city.rdd.map(lambda r:(r['ID'],r['Name']))
ans = country_rdd.join(city_rdd).map(lambda r:r[1]).collect()
for item in ans:
    print(item[0]+'    '+item[1])