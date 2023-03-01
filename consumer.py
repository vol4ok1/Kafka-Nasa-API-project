
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import json


# RUN COMMAND : spark-submit --deploy-mode cluster --master yarn consumer.py
# CHECK LOG :  yarn logs -applicationId application_1667920179011_4100
# Check folder : hdfs dfs -ls interns/

topic_apod = "api.analyst_data.apod_edvin"
topic_insight = "api.analyst_data.insight_edvin"

file_path_apod = r"interns/test/landing/apod_edvin_test/" + topic_apod + r"_landing"
file_path_insight = r"interns/test/landing/insight_edvin_test/" + topic_insight  + r"_landing"

checkpoint_apod_path = r"/interns/checkpoint/test/" + topic_apod + r'_test/'
checkpoint_insight_path = r"/interns/checkpoint/test/" + topic_insight + r'_test/'

def main():
    # Create sparksession
    spark = SparkSession \
        .builder \
        .appName("Kafka Consumer") \
        .getOrCreate()

    # Reads data from "Kafka topic" using SparkSession
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "node1.cloudera:9092") \
        .option("subscribe", topic_apod) \
        .option("startingOffsets", "earliest") \
        .option("failOnDataLoss", "false") \
        .load()
    
    #Creating readable data
    df1 = (df
       .withColumn("key", df["key"].cast(StringType()))
       .withColumn("value", df["value"].cast(StringType())))

    df1.writeStream   \
        .format("json")\
        .option("path", file_path_apod) \
        .option("checkpointLocation", checkpoint_apod_path) \
        .start() \
        .awaitTermination(10)
        
#This one run's insight with designated path
def main2():
    df2 = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "node1.cloudera:9092") \
        .option("subscribe", 'topic_insight') \
        .option("startingOffsets", "earliest") \
        .option("failOnDataLoss", "false") \
        .load()
    
    #Creating readable data
    df3 = (df2
       .withColumn("key", df["key"].cast(StringType()))
       .withColumn("value", df["value"].cast(StringType())))

    df3.writeStream   \
        .format("json")\
        .option("path", 'file_path_apod') \
        .option("checkpointLocation", checkpoint_insight_path) \
        .start() \
        .awaitTermination(10)
    