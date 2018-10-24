#!/usr/bin/env python
import sys
import boto
from boto.s3.key import Key
from pyspark.sql import *
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

  # create Spark context with Spark configuration
  conf = SparkConf().setAppName("Spark Count")
  sc = SparkContext(conf=conf)
  spark = SparkSession.builder.getOrCreate()

  df = spark.read.json(sys.argv[1])

  #get an RDD of the post titles
  rddTitles = df.select("data").rdd.map(lambda row: row[0]["title"].encode('utf-8').strip())
  
  #count unique titles and return a map of (title, count) pairs
  rddCounts = rddTitles.countByValue()
  
  #sort by titles ascending
  sortedItems = sorted(rddCounts.items(), reverse=False, key=lambda dct: dct[0])
  
  #sort by counts descending
  sortedItems = sorted(sortedItems, reverse=True, key=lambda dct: dct[1])
  
  #create report text
  text = ""
  for item in sortedItems:
    text += "%i  -  %s\n" % (item[1], item[0])

  #write to S3
  conn = boto.connect_s3(host="s3.amazonaws.com")
  bucket = conn.get_bucket("testing-datapipe")
  k = Key(bucket)
  k.key = "output/posts_num_days_report.txt"
  k.set_contents_from_string(text)
