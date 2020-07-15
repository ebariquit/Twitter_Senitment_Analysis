from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext

sc = SparkContext()

ssc = StreamingContext(sc, 10)
sqlContext = SQLContext(sc)

socket_stream = ssc.socketTextStream("127.0.0.1", 5555)

lines = socket_stream.window(60)

