import re
from pyspark import SparkContext,SparkConf


def normalizeWords(text):
    return re.compile(r'\W+',re.UNICODE).split(text.lower())


conf=SparkConf().setMaster("local").setAppName("wordCount")
sc=SparkContext(conf=conf)

input=sc.textFile("/home/venkat/Documents/Repo_Download/spark_course_1/Book.txt")
words=input.flatMap(normalizeWords)

#//wordsbycount eg word,1 then multiple occurance add word,5
wordCounts=words.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
#sorting by key and interchanging value to 5,word
wordCountsSorted=wordCounts.map(lambda x:(x[1],x[0])).sortByKey()
results=wordCountsSorted.collect()

for result in results:
    count=str(result[0])
    word=result[1].encode('ascii','ignore')
    if (word):
        print(word.decode()+':\t'+count)