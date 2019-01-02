from pyspark import SparkContext,SparkConf
import collections

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
    return (stationID, entryType, temperature)


#format in file is stationid,date,tmin/tmax,temp
lines=sc.textFile("/home/venkat/Documents/Repo_Download/spark_course_1/1800.csv")
#converting it into stationid,entrytype(tmin/tamx),temp
parsedLines=lines.map(parseLine)
#need to filter out tmin because our aim is to find out lowest temp in each station
minTemps=parsedLines.filter(lambda x:"TMIN" in x[1])
#so now minTemps has only Tmin of each station.now we need to find min temp for each station
stationTemps=minTemps.map(lambda x:(x[0],x[2]))
#now stationTemps has only stationID,temp key value pair
minTemps=stationTemps.reduceByKey(lambda x,y:min(x,y))
results=minTemps.collect()

for result in results:
    print(result[0]+"  {:.2f}F".format(result[1]))