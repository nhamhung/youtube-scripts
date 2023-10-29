# Create S3 bucket

- Persistent storage

- Can be used to store data input, script, output, cluster logs

# Create an EMR cluster

- Spark 3.4.0 on Hadoop 3.3.3 YARN with and Zeppelin 0.10.1

- 1 Primary, 1 Core, 1 Task

# Check created EC2 instances

# Allow SSH into Nodes

Set up inbound SSH connection through port 22

- `Properties -> EC2 Security Groups -> SSH TCP port 22 -> My IP`

# Connect to Primary Node to prepare script and data

- `ssh -i ~/.ssh/my-key-pair.pem hadoop@ec2-3-0-180-157.ap-southeast-1.compute.amazonaws.com`

View cluster setup:

- Executable: `/usr/bin/spark-shell`
- Config: `/etc/spark/conf/`
- Installation: `/usr/lib/spark`

# Enable dynamic port forwarding through SOCKS SSH connection

1. Enable port forwarding `ssh -i ~/.ssh/my-key-pair.pem -ND 8157 hadoop@ec2-3-0-180-157.ap-southeast-1.compute.amazonaws.com`
2. Set up Proxy SwitchyOmega: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-proxy.html

```
function FindProxyForURL(url, host) {
    if (shExpMatch(url, "*ec2*.*compute*.amazonaws.com*")) return 'SOCKS5 localhost:8157';
    if (shExpMatch(url, "*ec2*.compute*")) return 'SOCKS5 localhost:8157';
    if (shExpMatch(url, "http://10.*")) return 'SOCKS5 localhost:8157';
    if (shExpMatch(url, "*10*.compute*")) return 'SOCKS5 localhost:8157';
    if (shExpMatch(url, "*10*.amazonaws.com*")) return 'SOCKS5 localhost:8157';
    if (shExpMatch(url, "*.compute.internal*")) return 'SOCKS5 localhost:8157';
    if (shExpMatch(url, "*ec2.internal*")) return 'SOCKS5 localhost:8157';
    return 'DIRECT';
}
```

# View HDFS and YARN

- HDFS name node
- Resource manager
- Spark history server
- Zeppelin

# Prepare input data and script

Preview Spark script and data

- `script.py`
- `food_establishment_data.csv`

Transfer script and data to namenode

- `rsync -avz -e "ssh -i ~/.ssh/my-key-pair.pem" ~/Downloads/script.py hadoop@ec2-3-0-180-157.ap-southeast-1.compute.amazonaws.com:~/.`

- `rsync -avz -e "ssh -i ~/.ssh/my-key-pair.pem" ~/Downloads/food_establishment_data.csv hadoop@ec2-3-0-180-157.ap-southeast-1.compute.amazonaws.com:~/.`

Copy input file from local to HDFS

- `hadoop fs -copyFromLocal food_establishment_data.csv /user/hadoop/`

- `hadoop fs -ls /user/hadoop`

- `sudo du -h /mnt/hdfs`

- `sudo du -h /mnt1/hdfs`

Check HDFS file system UI

# Submit job to Spark

Run spark-submit command

`spark-submit --deploy-mode cluster script.py --data_source hdfs:///user/hadoop/food_establishment_data.csv --output_uri hdfs:///user/hadoop/output`

View submitted application in YARN

View Spark UI in Spark history server

Verify output with HDFS UI and pyspark shell

```
df = spark.read.option("header", "true").csv("/user/hadoop/output")
df.show(truncate=False)
```

# Try Zeppelin notebook

```
val restaurantViolations = spark.read.option("header", "true").csv("/user/hadoop/food_establishment_data.csv")


val resultDF = restaurantViolations
      .where(col("violation_type") === "RED")
      .groupBy(col("name"))
      .agg(count("*").alias("total_red_violations"))
      .orderBy(desc("total_red_violations"))
      .limit(10)

resultDF.show()

val output = spark.read.option("header", "true").csv("/user/hadoop/output")

output.show()
```

Also can view on YARN and Spark History Server

# View S3 cluster logs if necessary

# Terminate cluster
