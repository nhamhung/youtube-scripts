# Prepare common directory

```
sudo mkdir /usr/local/hadoop
sudo mkdir /usr/local/spark
sudo mkdir /usr/local/zeppelin

sudo chown -R nhamhhung:staff /usr/local/hadoop
sudo chown -R nhamhhung:staff /usr/local/spark
sudo chown -R nhamhhung:staff /usr/local/zeppelin
```

# Install Hadoop

## Checksum

```
shasum -c spark.checksum
shasum -c hadoop.checksum
shasum -c zeppelin.checksum
```

## Move Hadoop to directory

```
tar -xf hadoop-3.3.6.tar.gz
sudo mv hadoop-3.3.6/* /usr/local/hadoop
```

## Prepare common paths

```
# Copy to .zshrc or .bashrc
export JAVA_HOME="/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home"
export HADOOP_HOME="/usr/local/hadoop"
export PATH="$HOME/.jenv/bin:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH"

source ~/.zshrc
```

## Verify Hadoop and Java

```
hadoop
hdfs
java -version
```

## Make sure we can ssh to localhost without a passphrase

```
ssh localhost

https://stackoverflow.com/questions/17335728/connect-to-host-localhost-port-22-connection-refused
```

## Prepare Hadoop config

```
vim /usr/local/hadoop/etc/hadoop/hadoop-env.sh
export JAVA_HOME=/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
```

## Initialise HDFS

```
hdfs namenode -format
```

## Start NameNode and DataNode daemons

```
vim /usr/local/hadoop/etc/hadoop/core-site.xml
vim /usr/local/hadoop/etc/hadoop/hdfs-site.xml
start-dfs.sh
jps

# Check http://localhost:9870/
```

## Prepare HDFS directory

```
hdfs dfs -mkdir -p /user/nhamhhung
```

## Start Yarn

```
vim /usr/local/hadoop/etc/hadoop/mapred-site.xml
vim /usr/local/hadoop/etc/hadoop/yarn-site.xml
start-yarn.sh
jps

# Check http://localhost:8088/cluster
```

## Submit MapReduce job to Yarn

```
hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar grep input output 'dfs[a-z.]+'
```

# Install Spark

## Move Spark to directory

```
sudo mv spark-3.3.3-bin-hadoop3/* /usr/local/spark
```

## Prepare Spark path

```
# Copy to .zshrc or .bashrc
export SPARK_HOME=/usr/local/spark
export PATH="$HOME/.jenv/bin:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SPARK_HOME/bin:$PATH"
```

## Prepare Spark config

```
cp /usr/local/spark/conf/spark-env.sh.template /usr/local/spark/conf/spark-env.sh
vim /usr/local/spark/conf/spark-env.sh

HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop
```

## Run Spark on Yarn

```
spark-shell --master yarn --deploy-mode client
```

# Install Zeppelin

## Move Zeppelin to directory

```
sudo mv zeppelin-0.10.1-bin-netinst/* /usr/local/zeppelin
```

## Prepare Zeppelin path

```
# Copy to .zshrc or .bashrc
export ZEPPELIN_HOME=/usr/local/zeppelin
export PATH="$HOME/.jenv/bin:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SPARK_HOME/bin:$ZEPPELIN_HOME/bin:$PATH"
```

## Prepare Zeppelin config

```
cp /usr/local/zeppelin/conf/zeppelin-env.sh.template /usr/local/zeppelin/conf/zeppelin-env.sh
vim /usr/local/zeppelin/conf/zeppelin-env.sh

JAVA_HOME=/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
USE_HADOOP=true
export HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop
```

## Run Zeppelin

```
zeppelin-daemon.sh start

# Check http://localhost:8080/#/
```

## Prepare Spark interpreter

```
spark.master=yarn
spark.submit.deployMode=client
zeppelin.spark.enableSupportedVersionCheck=false
```

# Revert to original state

```
rm -rf /tmp/hadoop-nhamhhung
stop-all.sh
sudo rm -r /usr/local/hadoop
sudo rm -r /usr/local/spark
sudo rm -r /usr/local/zeppelin
```
