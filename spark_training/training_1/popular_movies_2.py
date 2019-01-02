from pyspark import SparkContext,SparkConf

def loadMovieNames():
    movieNames = {}
    with open("/home/venkat/Documents/Repo_Download/spark_course_1/ml-100k/u.item", encoding = "ISO-8859-1") as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
    return movieNames


conf=SparkConf().setMaster("local").setAppName("popular_movies")
sc=SparkContext(conf=conf)

#broadcasting namedict to all executors,dict has movie id and name
nameDict=sc.broadcast(loadMovieNames())

#movies u.data has userid,movieid,rating,timestamp
#goal is to find the most popular movie
lines=sc.textFile("/home/venkat/Documents/Repo_Download/spark_course_1/ml-100k/u.data")
#movies has movieid and 1
movies=lines.map(lambda x:(int(x.split()[1]),1))
#moviescount will have movieid and count of occurance
moviescount=movies.reduceByKey(lambda x,y:x+y)
#now need to sort moviescount in rddd by shuffling count and movieid
sortedmoviescount=moviescount.map(lambda x:(x[1],x[0])).sortByKey()

#convert count and movie id to movie name and count
#.value to get broadcast variable sent to all executors
sortedMoviesWithNames=sortedmoviescount.map(lambda x:(nameDict.value[x[1]],x[0]))
results=sortedMoviesWithNames.collect()

#printing count and movieid
for result in results:
    print(result)