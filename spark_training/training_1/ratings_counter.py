from pyspark import  SparkConf,SparkContext
import collections



conf=SparkConf().setMaster("local").setAppName("Ratings Histogram")
sc=SparkContext(conf=conf)


lines=sc.textFile("/home/venkat/Documents/Repo_Download/spark_course_1/ml-100k/u.data")
ratings=lines.map(lambda x:x.split()[2])
result=ratings.countByValue()

sortedResults=collections.OrderedDict(sorted(result.items()))
for key,value in sortedResults.items():
    print("%s %i"%(key,value))