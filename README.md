# Twitter_Senitment_Analysis
Analyzes the sentiment of Tweets in real-time (as they are published to Twitter).

# Requirements
 - Python (3.8.2)
 - Tweepy (3.9.0) + Twitter account with developer access
 - Apache Spark (3.0.0)
 - PySpark (3.0.0)
 - Matplotlib (3.2.2)
 - Pandas (1.0.5) 
 - MySQL Server
 - C#
 - Linux (Ubuntu 20.04)


# Installation
1. Download Tweepy: http://docs.tweepy.org/en/latest/install.html.
2. Download Apache Spark: https://phoenixnap.com/kb/install-spark-on-ubuntu.
    - Note: replace all references to spark version 2.4.5, with references to version 3.0.0
3. Download PySpark: https://pypi.org/project/pyspark/.
4. Clone this repository.
5. Create a config.ini file, filling it with the credentials provided by your Twitter Developer account. Note: my config.ini file is not included in the repository, for obvious security concerns.

# Running
1. Run the tweepy_test.py and spark_test.py files to test that you have correctly setup your requirements.
2. If everything is working, run tweepy_to_spark.py.
3. When you get the message "Socket created. Listening on port: 9009" (or whatever port you are using), run spark__.py.
