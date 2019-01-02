from pyspark import SparkContext,SparkConf

#goal is to find most popular superhero
conf=SparkConf().setMaster("local").setAppName("most_pop_superhero")
sc=SparkContext(conf=conf)

#2nd file has hero id and name
#returning key value pair
def parseNames(line):
    fields=line.split('\"')
    return (int(fields[0]),fields[1].encode("utf8"))


names=sc.textFile("/home/venkat/Documents/Repo_Download/spark_course_1/Marvel-Names.txt")
namesRdd=names.map(parseNames)


def loadHeroWithOccurances(line):
    elements=line.split()
    return (int(elements[0]),len(elements)-1)

#there are 2 files with marvel graph having superheroid with cooccurances


lines=sc.textFile("/home/venkat/Documents/Repo_Download/spark_course_1/Marvel-Graph.txt")
#has hero id and occurances and then reduce by key because multiple rows may have same hero
heroIdsWithOccurances=lines.map(loadHeroWithOccurances).reduceByKey(lambda x,y:x+y)
#change occurances to key to sort so flipped has occurances and super heroids
flipped=heroIdsWithOccurances.map(lambda x:(x[1],x[0]))

mostpopular=flipped.max()
#lookup is used to get max values passing id and getting name which has 1 string so [0]
mostpopularname=namesRdd.lookup(mostpopular[1])[0]

print(str(mostpopularname)+" has "+ str(mostpopular[0])+" co-appearances.")