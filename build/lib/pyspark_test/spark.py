from pyspark.sql import SparkSession
from functools import lru_cache
from pyspark import SparkContext

@lru_cache(maxsize=None)
def get_spark():
    return (SparkSession.builder
                .master("local")
                .appName("test")
                .getOrCreate())

@lru_cache(maxsize=None)
def get_sc():
    return (SparkContext(master="local", appName="test" ).getOrCreate())