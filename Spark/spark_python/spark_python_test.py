#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/22 下午12:28
# @Author  : Aries
# @Site    : 
# @File    : spark_python_test.py
# @Software: PyCharm

from pyspark.sql import SparkSession

log_file = "./README.md" # File on our System.
appName = "spark_app"
master = "local"
spark = SparkSession.builder.appName(name=appName).master(master=master).getOrCreate()
log_data = spark.read.text(log_file).cache()

numA = log_data.filter(log_data.value.contains('a')).count()
numB = log_data.filter(log_data.value.contains('b')).count()

print("lines with a is : %d " % numA)
print("lines with b is : %d " % numB)

print("============================================================================")

spark.stop()