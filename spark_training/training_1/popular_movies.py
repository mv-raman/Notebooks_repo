from pyspark import SparkContext,SparkConf

conf=SparkConf().setMaster("local").setAppName("popular_movies")
sc=SparkContext(conf=conf)

#movies u.data has userid,movieid,rating,timestamp
#goal is to find the most popular movie
lines=sc.textFile("/home/venkat/Documents/Repo_Download/spark_course_1/ml-100k/u.data")
#movies has movieid and 1
movies=lines.map(lambda x:(int(x.split()[1]),1))
#moviescount will have movieid and count of occurance
moviescount=movies.reduceByKey(lambda x,y:x+y)
#now need to sort moviescount in rddd by shuffling count and movieid
sortedmoviescount=moviescount.map(lambda x:(x[1],x[0])).sortByKey()
results=sortedmoviescount.collect()

#printing count and movieid
for result in results:
    print(result)