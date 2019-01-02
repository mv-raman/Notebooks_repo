from pyspark import SparkConf,SparkContext

conf=SparkConf().setMaster("local").setAppName("wordCount")
sc=SparkContext(conf=conf)


input=sc.textFile("/home/venkat/Documents/Repo_Download/spark_course_1/Book.txt")
words=input.flatMap(lambda x:x.split())
wordCounts=words.countByValue()

for word,count in wordCounts.items():
    cleanWord=word.encode("ascii","ignore")
    if(cleanWord):
        print(word+" "+str(count))