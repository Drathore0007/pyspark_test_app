from pyspark_test.spark import get_sc
import sys

def wordcount():
    #file = sys.argv[1]
    rdd = get_sc().textFile("file://home/dharm/Documents/Dr. Heinz Doofenshmirtz_Evil_corp_Develpoment/GitHub/pyspark_test/pyspark_test/wordcount.py")
    return rdd.flatMap(lambda line: line.split(" "))\
                  .map(lambda word: (word, 1))\
                  .reduceByKey(lambda a, b: a+b).count

if __name__ == '__main__':
    wordcount()