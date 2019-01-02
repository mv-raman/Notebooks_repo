from pyspark import SparkContext,SparkConf
import collections

conf=SparkConf().setMaster("local").setAppName("FriendsByAge")
sc=SparkContext(conf=conf)

def parseLine(line):
    fields=line.split(',')
    age=int(fields[2])
    numFriends=int(fields[3])
    return age,numFriends

lines=sc.textFile("/home/venkat/Documents/Repo_Download/spark_course_1/fakefriends.csv")
rdd=lines.map(parseLine)

totalsByAge=rdd.mapValues(lambda x:(x,1)).reduceByKey(lambda x,y:(x[0]+y[0],x[1]+y[1]))
averagesByAge=totalsByAge.mapValues(lambda x:x[0]/x[1])

results=averagesByAge.collect()

sortedResults=collections.OrderedDict(sorted(results))
for key,value in sortedResults.items():
    print("%s %i"%(key,value))