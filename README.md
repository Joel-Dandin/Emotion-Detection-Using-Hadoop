# Emotion Detection Using Hadoop

Hadoop Streaming is a feature that comes with Hadoop that enables users or developers to use a variety of different languages, such as Python, C++, Ruby, and others, to write MapReduce programs. All languages that can read from and write to standard input and output are supported. Python will be used with Hadoop Streaming, and we'll see how it performs. To comprehend Hadoop Streaming, we will use the word count problem as a Python implementation. To carry out map and reduce duties, we will create the scripts mapper.py and reducer.py.

We use MapReduce process to classify amazon product reviews into 5 catogries namely

-> Best  
-> Good  
-> Average  
-> Bad  
-> Worst  

# Build using Docker

## Pull the image
```
docker pull fedric/hadoop-spark-pig-hive
```

## Start a container
In order to use the Docker image you have just build or pulled use:
```
docker run -it -p 50070:50070 -p 8088:8088 -p 8080:8080 fedric/hadoop-spark-pig-hive bash
```

# Running the programs 

## Run emotion detection on Test data

Clone Repository into the system
```
git clone https://github.com/Joel-Fedric/emotion-detection-using-hadoop.git
```

Create Directory in Hadoop HDFS to load data for processing
```
hadoop fs -mkdir /user
hadoop fs -mkdir /user/Review
hadoop fs -mkdir /user/Summary
hadoop fs -mkdir /user/Overall
```

Verify directory created 
```
hadoop fs -ls / 
```

You can use data provided in the repositoy or creat own data using using amazon's review dataset from [https://snap.stanford.edu/data/web-Amazon.html](https://snap.stanford.edu/data/web-Amazon.html)  
OR  
Use the Python Notebook (Create data.ipynb) to collect the data form above site and create sub folders with only data form Review, Summary, and Overall of the data set for each individual products.

Upload data from local storage to HDFS
```
hdfs dfs -copyFromLocal /Data/Review/* /user/Review
hdfs dfs -copyFromLocal /Data/Summary/* /user/Summary
hdfs dfs -copyFromLocal /Data/Overall/* /user/Overall
```

Download the jar file requires for hadoop streaming [Jar file](https://jar-download.com/artifacts/org.apache.hadoop/hadoop-streaming/2.7.3/source-code)  
OR  
Use the jar file given in the reposotery

Start Map-Reduce process to get results for one of the file
```
hadoop jar hadoop-streaming-2.7.3.jar -input /user/Review/B003AVMZA4.txt -output /user/ReviewOutput -mapper mapper.py -reducer reducer.py 
```

Read the output results
```
hdfs dfs -cat /user/ReviewOutput/part-00000
```
