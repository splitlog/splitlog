from io import BytesIO

from splitlog import split
from tests import InMemoryOutputFolder

INPUT_FIXTURE = b"""Container: container_1671326373437_0001_01_000003 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:directory.info
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:1937
LogContents:
ls -l:
total 32
-rw-r--r-- 1 yarn yarn  129 Dec 18 01:27 container_tokens
-rwx------ 1 yarn yarn  627 Dec 18 01:27 default_container_executor_session.sh
-rwx------ 1 yarn yarn  682 Dec 18 01:27 default_container_executor.sh
lrwxrwxrwx 1 yarn yarn   97 Dec 18 01:27 job.jar -> /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/11/job.jar
lrwxrwxrwx 1 yarn yarn   97 Dec 18 01:27 job.xml -> /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/13/job.xml
-rwx------ 1 yarn yarn 4932 Dec 18 01:27 launch_container.sh
drwx--x--- 2 yarn yarn 4096 Dec 18 01:27 tmp
find -L . -maxdepth 5 -ls:
 63318185      4 drwx--x---   3 yarn     yarn         4096 Dec 18 01:27 .
 63318187      4 drwx--x---   2 yarn     yarn         4096 Dec 18 01:27 ./tmp
 63318194      4 -rwx------   1 yarn     yarn          682 Dec 18 01:27 ./default_container_executor.sh
 63318192      4 -rwx------   1 yarn     yarn          627 Dec 18 01:27 ./default_container_executor_session.sh
 63318191      4 -rw-r--r--   1 yarn     yarn           48 Dec 18 01:27 ./.launch_container.sh.crc
 63317898      4 drwx------   2 yarn     yarn         4096 Dec 18 01:27 ./job.jar
 63317919    276 -r-x------   1 yarn     yarn       280992 Dec 18 01:27 ./job.jar/job.jar
 63318193      4 -rw-r--r--   1 yarn     yarn           16 Dec 18 01:27 ./.default_container_executor_session.sh.crc
 63318115    232 -r-x------   1 yarn     yarn       235968 Dec 18 01:27 ./job.xml
 63318188      4 -rw-r--r--   1 yarn     yarn          129 Dec 18 01:27 ./container_tokens
 63318190      8 -rwx------   1 yarn     yarn         4932 Dec 18 01:27 ./launch_container.sh
 63318189      4 -rw-r--r--   1 yarn     yarn           12 Dec 18 01:27 ./.container_tokens.crc
 63318195      4 -rw-r--r--   1 yarn     yarn           16 Dec 18 01:27 ./.default_container_executor.sh.crc
broken symlinks(find -L . -maxdepth 5 -type l -ls):

End of LogType:directory.info
*******************************************************************************

Container: container_1671326373437_0001_01_000003 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:launch_container.sh
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:4932
LogContents:
#!/bin/bash

set -o pipefail -e
export PRELAUNCH_OUT="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/prelaunch.out"
exec >"${PRELAUNCH_OUT}"
export PRELAUNCH_ERR="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/prelaunch.err"
exec 2>"${PRELAUNCH_ERR}"
echo "Setting up env variables"
export JAVA_HOME=${JAVA_HOME:-"/opt/java/openjdk"}
export HADOOP_COMMON_HOME=${HADOOP_COMMON_HOME:-"/hadoop"}
export HADOOP_HDFS_HOME=${HADOOP_HDFS_HOME:-"/hadoop"}
export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/hadoop/etc/hadoop"}
export HADOOP_YARN_HOME=${HADOOP_YARN_HOME:-"/hadoop"}
export HADOOP_HOME=${HADOOP_HOME:-"/hadoop"}
export PATH=${PATH:-"/hadoop/bin:/hadoop/sbin:/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"}
export LANG=${LANG:-"en_US.UTF-8"}
export HADOOP_MAPRED_HOME=${HADOOP_MAPRED_HOME:-"/hadoop"}
export HADOOP_TOKEN_FILE_LOCATION="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000003/container_tokens"
export CONTAINER_ID="container_1671326373437_0001_01_000003"
export NM_PORT="36113"
export NM_HOST="hadoopnode"
export NM_HTTP_PORT="8042"
export LOCAL_DIRS="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001"
export LOCAL_USER_DIRS="/data/nm-local-dir/usercache/sandbox/"
export LOG_DIRS="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003"
export USER="sandbox"
export LOGNAME="sandbox"
export HOME="/home/"
export PWD="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000003"
export LOCALIZATION_COUNTERS="0,518812,0,2,1"
export JVM_PID="$$"
export NM_AUX_SERVICE_mapreduce_shuffle="AAA0+gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
export STDOUT_LOGFILE_ENV="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/stdout"
export SHELL="/bin/bash"
export HADOOP_ROOT_LOGGER="INFO,console"
export CLASSPATH="$PWD:$HADOOP_CONF_DIR:$HADOOP_COMMON_HOME/share/hadoop/common/*:$HADOOP_COMMON_HOME/share/hadoop/common/lib/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/lib/*:$HADOOP_YARN_HOME/share/hadoop/yarn/*:$HADOOP_YARN_HOME/share/hadoop/yarn/lib/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*:job.jar/*:job.jar/classes/:job.jar/lib/*:$PWD/*"
export LD_LIBRARY_PATH="$PWD:$HADOOP_COMMON_HOME/lib/native"
export STDERR_LOGFILE_ENV="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/stderr"
export HADOOP_CLIENT_OPTS=""
export MALLOC_ARENA_MAX="4"
echo "Setting up job resources"
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/11/job.jar" "job.jar"
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/13/job.xml" "job.xml"
echo "Copying debugging information"
# Creating copy of launch script
cp "launch_container.sh" "/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/launch_container.sh"
chmod 640 "/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/launch_container.sh"
# Determining directory contents
echo "ls -l:" 1>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/directory.info"
ls -l 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/directory.info"
echo "find -L . -maxdepth 5 -ls:" 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/directory.info"
find -L . -maxdepth 5 -ls 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/directory.info"
echo "broken symlinks(find -L . -maxdepth 5 -type l -ls):" 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/directory.info"
find -L . -maxdepth 5 -type l -ls 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/directory.info"
echo "Launching container"
exec /bin/bash -c "$JAVA_HOME/bin/java -Djava.net.preferIPv4Stack=true -Dhadoop.metrics.log.level=WARN   -Xmx820m -Djava.io.tmpdir=$PWD/tmp -Dlog4j.configuration=container-log4j.properties -Dyarn.app.container.log.dir=/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003 -Dyarn.app.container.log.filesize=0 -Dhadoop.root.logger=INFO,CLA -Dhadoop.root.logfile=syslog org.apache.hadoop.mapred.YarnChild 10.0.1.4 45261 attempt_1671326373437_0001_m_000001_0 3 1>/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/stdout 2>/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/stderr "

End of LogType:launch_container.sh
************************************************************************************

Container: container_1671326373437_0001_01_000003 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:prelaunch.err
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:0
LogContents:

End of LogType:prelaunch.err
******************************************************************************

Container: container_1671326373437_0001_01_000003 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:prelaunch.out
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:100
LogContents:
Setting up env variables
Setting up job resources
Copying debugging information
Launching container

End of LogType:prelaunch.out
******************************************************************************

Container: container_1671326373437_0001_01_000003 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:stderr
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:0
LogContents:

End of LogType:stderr
***********************************************************************

Container: container_1671326373437_0001_01_000003 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:stdout
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:0
LogContents:

End of LogType:stdout
***********************************************************************

Container: container_1671326373437_0001_01_000003 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:syslog
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:23202
LogContents:
2022-12-18 01:27:34,652 INFO [main] org.apache.hadoop.security.SecurityUtil: Updating Configuration
2022-12-18 01:27:34,705 INFO [main] org.apache.hadoop.metrics2.impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2022-12-18 01:27:34,749 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 second(s).
2022-12-18 01:27:34,750 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MapTask metrics system started
2022-12-18 01:27:34,782 INFO [main] org.apache.hadoop.mapred.YarnChild: Executing with tokens: [Kind: mapreduce.job, Service: job_1671326373437_0001, Ident: (org.apache.hadoop.mapreduce.security.token.JobTokenIdentifier@1ebd319f)]
2022-12-18 01:27:34,807 INFO [main] org.apache.hadoop.mapred.YarnChild: Sleeping for 0ms before retrying again. Got null now.
2022-12-18 01:27:34,910 INFO [main] org.apache.hadoop.mapred.YarnChild: mapreduce.cluster.local.dir for child: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001
2022-12-18 01:27:35,049 INFO [main] org.apache.hadoop.mapred.YarnChild: 
/************************************************************
[system properties]
os.name: Linux
os.version: 6.0.0-6-amd64
java.home: /opt/java/openjdk/jre
java.runtime.version: 1.8.0_345-b01
java.vendor: Temurin
java.version: 1.8.0_345
java.vm.name: OpenJDK 64-Bit Server VM
java.class.path: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000003:/hadoop/etc/hadoop:/hadoop/share/hadoop/common/hadoop-nfs-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-kms-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-registry-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-common-3.3.4-tests.jar:/hadoop/share/hadoop/common/hadoop-common-3.3.4.jar:/hadoop/share/hadoop/common/lib/kerby-pkix-1.0.1.jar:/hadoop/share/hadoop/common/lib/nimbus-jose-jwt-9.8.1.jar:/hadoop/share/hadoop/common/lib/jetty-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/asm-5.0.4.jar:/hadoop/share/hadoop/common/lib/paranamer-2.3.jar:/hadoop/share/hadoop/common/lib/commons-configuration2-2.1.1.jar:/hadoop/share/hadoop/common/lib/kerb-identity-1.0.1.jar:/hadoop/share/hadoop/common/lib/re2j-1.1.jar:/hadoop/share/hadoop/common/lib/jackson-xc-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-beanutils-1.9.4.jar:/hadoop/share/hadoop/common/lib/jsch-0.1.55.jar:/hadoop/share/hadoop/common/lib/commons-math3-3.1.1.jar:/hadoop/share/hadoop/common/lib/jackson-mapper-asl-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-security-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-codec-1.15.jar:/hadoop/share/hadoop/common/lib/gson-2.8.9.jar:/hadoop/share/hadoop/common/lib/j2objc-annotations-1.1.jar:/hadoop/share/hadoop/common/lib/jackson-core-asl-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-webapp-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/animal-sniffer-annotations-1.17.jar:/hadoop/share/hadoop/common/lib/jackson-jaxrs-1.9.13.jar:/hadoop/share/hadoop/common/lib/kerby-util-1.0.1.jar:/hadoop/share/hadoop/common/lib/zookeeper-3.5.6.jar:/hadoop/share/hadoop/common/lib/accessors-smart-2.4.7.jar:/hadoop/share/hadoop/common/lib/reload4j-1.2.22.jar:/hadoop/share/hadoop/common/lib/jcip-annotations-1.0-1.jar:/hadoop/share/hadoop/common/lib/jersey-servlet-1.19.jar:/hadoop/share/hadoop/common/lib/metrics-core-3.2.4.jar:/hadoop/share/hadoop/common/lib/jersey-json-1.19.jar:/hadoop/share/hadoop/common/lib/jsp-api-2.1.jar:/hadoop/share/hadoop/common/lib/curator-client-4.2.0.jar:/hadoop/share/hadoop/common/lib/curator-recipes-4.2.0.jar:/hadoop/share/hadoop/common/lib/commons-text-1.4.jar:/hadoop/share/hadoop/common/lib/jersey-server-1.19.jar:/hadoop/share/hadoop/common/lib/kerb-simplekdc-1.0.1.jar:/hadoop/share/hadoop/common/lib/jersey-core-1.19.jar:/hadoop/share/hadoop/common/lib/avro-1.7.7.jar:/hadoop/share/hadoop/common/lib/commons-io-2.8.0.jar:/hadoop/share/hadoop/common/lib/kerb-core-1.0.1.jar:/hadoop/share/hadoop/common/lib/slf4j-api-1.7.36.jar:/hadoop/share/hadoop/common/lib/kerb-server-1.0.1.jar:/hadoop/share/hadoop/common/lib/commons-collections-3.2.2.jar:/hadoop/share/hadoop/common/lib/jackson-core-2.12.7.jar:/hadoop/share/hadoop/common/lib/commons-daemon-1.0.13.jar:/hadoop/share/hadoop/common/lib/snappy-java-1.1.8.2.jar:/hadoop/share/hadoop/common/lib/jettison-1.1.jar:/hadoop/share/hadoop/common/lib/kerb-common-1.0.1.jar:/hadoop/share/hadoop/common/lib/jetty-http-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/failureaccess-1.0.jar:/hadoop/share/hadoop/common/lib/jul-to-slf4j-1.7.36.jar:/hadoop/share/hadoop/common/lib/jaxb-api-2.2.11.jar:/hadoop/share/hadoop/common/lib/jsr311-api-1.1.1.jar:/hadoop/share/hadoop/common/lib/jaxb-impl-2.2.3-1.jar:/hadoop/share/hadoop/common/lib/javax.servlet-api-3.1.0.jar:/hadoop/share/hadoop/common/lib/zookeeper-jute-3.5.6.jar:/hadoop/share/hadoop/common/lib/jetty-util-ajax-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-compress-1.21.jar:/hadoop/share/hadoop/common/lib/commons-net-3.6.jar:/hadoop/share/hadoop/common/lib/commons-cli-1.2.jar:/hadoop/share/hadoop/common/lib/checker-qual-2.5.2.jar:/hadoop/share/hadoop/common/lib/jetty-io-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/netty-3.10.6.Final.jar:/hadoop/share/hadoop/common/lib/kerb-crypto-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerby-asn1-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerby-xdr-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerb-util-1.0.1.jar:/hadoop/share/hadoop/common/lib/commons-logging-1.1.3.jar:/hadoop/share/hadoop/common/lib/commons-lang3-3.12.0.jar:/hadoop/share/hadoop/common/lib/token-provider-1.0.1.jar:/hadoop/share/hadoop/common/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/hadoop/share/hadoop/common/lib/jakarta.activation-api-1.2.1.jar:/hadoop/share/hadoop/common/lib/httpclient-4.5.13.jar:/hadoop/share/hadoop/common/lib/hadoop-shaded-guava-1.1.1.jar:/hadoop/share/hadoop/common/lib/hadoop-annotations-3.3.4.jar:/hadoop/share/hadoop/common/lib/hadoop-auth-3.3.4.jar:/hadoop/share/hadoop/common/lib/jackson-databind-2.12.7.jar:/hadoop/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar:/hadoop/share/hadoop/common/lib/curator-framework-4.2.0.jar:/hadoop/share/hadoop/common/lib/woodstox-core-5.3.0.jar:/hadoop/share/hadoop/common/lib/audience-annotations-0.5.0.jar:/hadoop/share/hadoop/common/lib/kerb-client-1.0.1.jar:/hadoop/share/hadoop/common/lib/json-smart-2.4.7.jar:/hadoop/share/hadoop/common/lib/dnsjava-2.1.7.jar:/hadoop/share/hadoop/common/lib/jsr305-3.0.2.jar:/hadoop/share/hadoop/common/lib/kerb-admin-1.0.1.jar:/hadoop/share/hadoop/common/lib/httpcore-4.4.13.jar:/hadoop/share/hadoop/common/lib/protobuf-java-2.5.0.jar:/hadoop/share/hadoop/common/lib/kerby-config-1.0.1.jar:/hadoop/share/hadoop/common/lib/jetty-util-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/jackson-annotations-2.12.7.jar:/hadoop/share/hadoop/common/lib/jetty-xml-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/hadoop-shaded-protobuf_3_7-1.1.1.jar:/hadoop/share/hadoop/common/lib/stax2-api-4.2.1.jar:/hadoop/share/hadoop/common/lib/guava-27.0-jre.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-native-client-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-rbf-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-rbf-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-native-client-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-httpfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-client-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-client-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-nfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/kerby-pkix-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/nimbus-jose-jwt-9.8.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/asm-5.0.4.jar:/hadoop/share/hadoop/hdfs/lib/paranamer-2.3.jar:/hadoop/share/hadoop/hdfs/lib/commons-configuration2-2.1.1.jar:/hadoop/share/hadoop/hdfs/lib/kerb-identity-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/re2j-1.1.jar:/hadoop/share/hadoop/hdfs/lib/jackson-xc-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/jetty-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-beanutils-1.9.4.jar:/hadoop/share/hadoop/hdfs/lib/leveldbjni-all-1.8.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-dns-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-rxtx-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jsch-0.1.55.jar:/hadoop/share/hadoop/hdfs/lib/commons-math3-3.1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-http2-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-udt-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jackson-mapper-asl-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/okhttp-4.9.3.jar:/hadoop/share/hadoop/hdfs/lib/jetty-security-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/commons-codec-1.15.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-mqtt-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-native-macos-4.1.77.Final-osx-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/gson-2.8.9.jar:/hadoop/share/hadoop/hdfs/lib/j2objc-annotations-1.1.jar:/hadoop/share/hadoop/hdfs/lib/jackson-core-asl-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/jetty-webapp-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/animal-sniffer-annotations-1.17.jar:/hadoop/share/hadoop/hdfs/lib/okio-2.8.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-handler-proxy-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jackson-jaxrs-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/kerby-util-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/zookeeper-3.5.6.jar:/hadoop/share/hadoop/hdfs/lib/accessors-smart-2.4.7.jar:/hadoop/share/hadoop/hdfs/lib/reload4j-1.2.22.jar:/hadoop/share/hadoop/hdfs/lib/jcip-annotations-1.0-1.jar:/hadoop/share/hadoop/hdfs/lib/jersey-servlet-1.19.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-kqueue-4.1.77.Final-osx-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/jersey-json-1.19.jar:/hadoop/share/hadoop/hdfs/lib/curator-client-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/curator-recipes-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/commons-text-1.4.jar:/hadoop/share/hadoop/hdfs/lib/kotlin-stdlib-common-1.4.10.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-unix-common-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-all-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-epoll-4.1.77.Final-linux-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/jersey-server-1.19.jar:/hadoop/share/hadoop/hdfs/lib/netty-common-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-simplekdc-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jersey-core-1.19.jar:/hadoop/share/hadoop/hdfs/lib/avro-1.7.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-io-2.8.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-haproxy-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-core-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-sctp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-server-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/commons-collections-3.2.2.jar:/hadoop/share/hadoop/hdfs/lib/jackson-core-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-http-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-daemon-1.0.13.jar:/hadoop/share/hadoop/hdfs/lib/snappy-java-1.1.8.2.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-classes-epoll-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jettison-1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-smtp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-common-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-http-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/failureaccess-1.0.jar:/hadoop/share/hadoop/hdfs/lib/kotlin-stdlib-1.4.10.jar:/hadoop/share/hadoop/hdfs/lib/jaxb-api-2.2.11.jar:/hadoop/share/hadoop/hdfs/lib/netty-buffer-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-classes-macos-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jsr311-api-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/json-simple-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-stomp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jaxb-impl-2.2.3-1.jar:/hadoop/share/hadoop/hdfs/lib/javax.servlet-api-3.1.0.jar:/hadoop/share/hadoop/hdfs/lib/zookeeper-jute-3.5.6.jar:/hadoop/share/hadoop/hdfs/lib/jetty-util-ajax-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-epoll-4.1.77.Final-linux-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/netty-handler-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-compress-1.21.jar:/hadoop/share/hadoop/hdfs/lib/commons-net-3.6.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-xml-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-cli-1.2.jar:/hadoop/share/hadoop/hdfs/lib/checker-qual-2.5.2.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-kqueue-4.1.77.Final-osx-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-memcache-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jetty-io-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-3.10.6.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-crypto-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerby-asn1-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerby-xdr-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerb-util-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/commons-logging-1.1.3.jar:/hadoop/share/hadoop/hdfs/lib/commons-lang3-3.12.0.jar:/hadoop/share/hadoop/hdfs/lib/token-provider-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/hadoop/share/hadoop/hdfs/lib/jakarta.activation-api-1.2.1.jar:/hadoop/share/hadoop/hdfs/lib/httpclient-4.5.13.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-redis-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-shaded-guava-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-annotations-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-auth-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/jackson-databind-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/curator-framework-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-native-macos-4.1.77.Final-osx-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/woodstox-core-5.3.0.jar:/hadoop/share/hadoop/hdfs/lib/audience-annotations-0.5.0.jar:/hadoop/share/hadoop/hdfs/lib/kerb-client-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/json-smart-2.4.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-socks-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-classes-kqueue-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/dnsjava-2.1.7.jar:/hadoop/share/hadoop/hdfs/lib/jsr305-3.0.2.jar:/hadoop/share/hadoop/hdfs/lib/kerb-admin-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/httpcore-4.4.13.jar:/hadoop/share/hadoop/hdfs/lib/protobuf-java-2.5.0.jar:/hadoop/share/hadoop/hdfs/lib/kerby-config-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-util-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/jackson-annotations-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/jetty-xml-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-shaded-protobuf_3_7-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/stax2-api-4.2.1.jar:/hadoop/share/hadoop/hdfs/lib/guava-27.0-jre.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-registry-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-router-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-client-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-distributedshell-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-services-core-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-nodemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-api-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-resourcemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-mawo-core-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-services-api-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-tests-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-unmanaged-am-launcher-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-sharedcachemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-web-proxy-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-timeline-pluginstorage-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-applicationhistoryservice-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-common-3.3.4.jar:/hadoop/share/hadoop/yarn/lib/javax.websocket-api-1.0.jar:/hadoop/share/hadoop/yarn/lib/websocket-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/json-io-2.5.1.jar:/hadoop/share/hadoop/yarn/lib/jline-3.9.0.jar:/hadoop/share/hadoop/yarn/lib/bcprov-jdk15on-1.60.jar:/hadoop/share/hadoop/yarn/lib/websocket-common-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jetty-jndi-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/websocket-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jackson-module-jaxb-annotations-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/HikariCP-java7-2.4.12.jar:/hadoop/share/hadoop/yarn/lib/jersey-client-1.19.jar:/hadoop/share/hadoop/yarn/lib/metrics-core-3.2.4.jar:/hadoop/share/hadoop/yarn/lib/jetty-client-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/guice-servlet-4.0.jar:/hadoop/share/hadoop/yarn/lib/swagger-annotations-1.5.4.jar:/hadoop/share/hadoop/yarn/lib/bcpkix-jdk15on-1.60.jar:/hadoop/share/hadoop/yarn/lib/websocket-api-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jna-5.2.0.jar:/hadoop/share/hadoop/yarn/lib/jackson-jaxrs-base-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/javax-websocket-client-impl-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/snakeyaml-1.26.jar:/hadoop/share/hadoop/yarn/lib/asm-tree-9.1.jar:/hadoop/share/hadoop/yarn/lib/javax.websocket-client-api-1.0.jar:/hadoop/share/hadoop/yarn/lib/javax-websocket-server-impl-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jackson-jaxrs-json-provider-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/asm-analysis-9.1.jar:/hadoop/share/hadoop/yarn/lib/websocket-client-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/ehcache-3.3.1.jar:/hadoop/share/hadoop/yarn/lib/guice-4.0.jar:/hadoop/share/hadoop/yarn/lib/fst-2.50.jar:/hadoop/share/hadoop/yarn/lib/jetty-plus-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jetty-annotations-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/geronimo-jcache_1.0_spec-1.0-alpha-1.jar:/hadoop/share/hadoop/yarn/lib/mssql-jdbc-6.2.1.jre7.jar:/hadoop/share/hadoop/yarn/lib/objenesis-2.6.jar:/hadoop/share/hadoop/yarn/lib/jersey-guice-1.19.jar:/hadoop/share/hadoop/yarn/lib/jakarta.xml.bind-api-2.3.2.jar:/hadoop/share/hadoop/yarn/lib/aopalliance-1.0.jar:/hadoop/share/hadoop/yarn/lib/javax.inject-1.jar:/hadoop/share/hadoop/yarn/lib/asm-commons-9.1.jar:/hadoop/share/hadoop/yarn/lib/java-util-1.9.0.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-plugins-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-shuffle-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.4-tests.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-nativetask-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-app-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-uploader-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.3.4.jar:/hadoop/share/hadoop/mapreduce/lib/*:job.jar/job.jar:job.jar/classes/:job.jar/lib/*:/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000003/job.jar
java.io.tmpdir: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000003/tmp
user.dir: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000003
user.name: yarn
************************************************************/
2022-12-18 01:27:35,049 INFO [main] org.apache.hadoop.conf.Configuration.deprecation: session.id is deprecated. Instead, use dfs.metrics.session-id
2022-12-18 01:27:35,256 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: File Output Committer Algorithm version is 2
2022-12-18 01:27:35,256 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2022-12-18 01:27:35,264 INFO [main] org.apache.hadoop.mapred.Task:  Using ResourceCalculatorProcessTree : [ ]
2022-12-18 01:27:35,338 INFO [main] org.apache.hadoop.mapred.MapTask: Processing split: org.apache.hadoop.examples.terasort.TeraGen$RangeInputFormat$RangeInputSplit@46f699d5
2022-12-18 01:27:35,684 INFO [main] org.apache.hadoop.mapred.Task: Task:attempt_1671326373437_0001_m_000001_0 is done. And is in the process of committing
2022-12-18 01:27:35,689 INFO [main] org.apache.hadoop.mapred.Task: Task attempt_1671326373437_0001_m_000001_0 is allowed to commit now
2022-12-18 01:27:35,697 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: Saved output of task 'attempt_1671326373437_0001_m_000001_0' to hdfs://namenode:8020/user/sandbox/teragen
2022-12-18 01:27:35,702 INFO [main] org.apache.hadoop.mapred.Task: Task 'attempt_1671326373437_0001_m_000001_0' done.
2022-12-18 01:27:35,706 INFO [main] org.apache.hadoop.mapred.Task: Final Counters for attempt_1671326373437_0001_m_000001_0: Counters: 27
	File System Counters
		FILE: Number of bytes read=0
		FILE: Number of bytes written=275762
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=85
		HDFS: Number of bytes written=50000000
		HDFS: Number of read operations=6
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Map-Reduce Framework
		Map input records=500000
		Map output records=500000
		Input split bytes=85
		Spilled Records=0
		Failed Shuffles=0
		Merged Map outputs=0
		GC time elapsed (ms)=33
		CPU time spent (ms)=1480
		Physical memory (bytes) snapshot=380235776
		Virtual memory (bytes) snapshot=2616180736
		Total committed heap usage (bytes)=606601216
		Peak Map Physical memory (bytes)=380235776
		Peak Map Virtual memory (bytes)=2616180736
	org.apache.hadoop.examples.terasort.TeraGen$Counters
		CHECKSUM=1074389572096518
	File Input Format Counters 
		Bytes Read=0
	File Output Format Counters 
		Bytes Written=50000000
2022-12-18 01:27:35,706 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: Stopping MapTask metrics system...
2022-12-18 01:27:35,707 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MapTask metrics system stopped.
2022-12-18 01:27:35,707 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MapTask metrics system shutdown complete.

End of LogType:syslog
***********************************************************************

Container: container_1671326373437_0001_01_000002 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:directory.info
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:1937
LogContents:
ls -l:
total 32
-rw-r--r-- 1 yarn yarn  129 Dec 18 01:27 container_tokens
-rwx------ 1 yarn yarn  627 Dec 18 01:27 default_container_executor_session.sh
-rwx------ 1 yarn yarn  682 Dec 18 01:27 default_container_executor.sh
lrwxrwxrwx 1 yarn yarn   97 Dec 18 01:27 job.jar -> /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/11/job.jar
lrwxrwxrwx 1 yarn yarn   97 Dec 18 01:27 job.xml -> /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/13/job.xml
-rwx------ 1 yarn yarn 4932 Dec 18 01:27 launch_container.sh
drwx--x--- 2 yarn yarn 4096 Dec 18 01:27 tmp
find -L . -maxdepth 5 -ls:
 63318156      4 drwx--x---   3 yarn     yarn         4096 Dec 18 01:27 .
 63318158      4 drwx--x---   2 yarn     yarn         4096 Dec 18 01:27 ./tmp
 63318165      4 -rwx------   1 yarn     yarn          682 Dec 18 01:27 ./default_container_executor.sh
 63318163      4 -rwx------   1 yarn     yarn          627 Dec 18 01:27 ./default_container_executor_session.sh
 63318162      4 -rw-r--r--   1 yarn     yarn           48 Dec 18 01:27 ./.launch_container.sh.crc
 63317898      4 drwx------   2 yarn     yarn         4096 Dec 18 01:27 ./job.jar
 63317919    276 -r-x------   1 yarn     yarn       280992 Dec 18 01:27 ./job.jar/job.jar
 63318164      4 -rw-r--r--   1 yarn     yarn           16 Dec 18 01:27 ./.default_container_executor_session.sh.crc
 63318115    232 -r-x------   1 yarn     yarn       235968 Dec 18 01:27 ./job.xml
 63318159      4 -rw-r--r--   1 yarn     yarn          129 Dec 18 01:27 ./container_tokens
 63318161      8 -rwx------   1 yarn     yarn         4932 Dec 18 01:27 ./launch_container.sh
 63318160      4 -rw-r--r--   1 yarn     yarn           12 Dec 18 01:27 ./.container_tokens.crc
 63318166      4 -rw-r--r--   1 yarn     yarn           16 Dec 18 01:27 ./.default_container_executor.sh.crc
broken symlinks(find -L . -maxdepth 5 -type l -ls):

End of LogType:directory.info
*******************************************************************************

Container: container_1671326373437_0001_01_000002 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:launch_container.sh
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:4932
LogContents:
#!/bin/bash

set -o pipefail -e
export PRELAUNCH_OUT="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/prelaunch.out"
exec >"${PRELAUNCH_OUT}"
export PRELAUNCH_ERR="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/prelaunch.err"
exec 2>"${PRELAUNCH_ERR}"
echo "Setting up env variables"
export JAVA_HOME=${JAVA_HOME:-"/opt/java/openjdk"}
export HADOOP_COMMON_HOME=${HADOOP_COMMON_HOME:-"/hadoop"}
export HADOOP_HDFS_HOME=${HADOOP_HDFS_HOME:-"/hadoop"}
export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/hadoop/etc/hadoop"}
export HADOOP_YARN_HOME=${HADOOP_YARN_HOME:-"/hadoop"}
export HADOOP_HOME=${HADOOP_HOME:-"/hadoop"}
export PATH=${PATH:-"/hadoop/bin:/hadoop/sbin:/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"}
export LANG=${LANG:-"en_US.UTF-8"}
export HADOOP_MAPRED_HOME=${HADOOP_MAPRED_HOME:-"/hadoop"}
export HADOOP_TOKEN_FILE_LOCATION="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000002/container_tokens"
export CONTAINER_ID="container_1671326373437_0001_01_000002"
export NM_PORT="36113"
export NM_HOST="hadoopnode"
export NM_HTTP_PORT="8042"
export LOCAL_DIRS="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001"
export LOCAL_USER_DIRS="/data/nm-local-dir/usercache/sandbox/"
export LOG_DIRS="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002"
export USER="sandbox"
export LOGNAME="sandbox"
export HOME="/home/"
export PWD="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000002"
export LOCALIZATION_COUNTERS="0,518812,0,2,3"
export JVM_PID="$$"
export NM_AUX_SERVICE_mapreduce_shuffle="AAA0+gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
export STDOUT_LOGFILE_ENV="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/stdout"
export SHELL="/bin/bash"
export HADOOP_ROOT_LOGGER="INFO,console"
export CLASSPATH="$PWD:$HADOOP_CONF_DIR:$HADOOP_COMMON_HOME/share/hadoop/common/*:$HADOOP_COMMON_HOME/share/hadoop/common/lib/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/lib/*:$HADOOP_YARN_HOME/share/hadoop/yarn/*:$HADOOP_YARN_HOME/share/hadoop/yarn/lib/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*:job.jar/*:job.jar/classes/:job.jar/lib/*:$PWD/*"
export LD_LIBRARY_PATH="$PWD:$HADOOP_COMMON_HOME/lib/native"
export STDERR_LOGFILE_ENV="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/stderr"
export HADOOP_CLIENT_OPTS=""
export MALLOC_ARENA_MAX="4"
echo "Setting up job resources"
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/11/job.jar" "job.jar"
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/13/job.xml" "job.xml"
echo "Copying debugging information"
# Creating copy of launch script
cp "launch_container.sh" "/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/launch_container.sh"
chmod 640 "/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/launch_container.sh"
# Determining directory contents
echo "ls -l:" 1>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/directory.info"
ls -l 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/directory.info"
echo "find -L . -maxdepth 5 -ls:" 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/directory.info"
find -L . -maxdepth 5 -ls 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/directory.info"
echo "broken symlinks(find -L . -maxdepth 5 -type l -ls):" 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/directory.info"
find -L . -maxdepth 5 -type l -ls 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/directory.info"
echo "Launching container"
exec /bin/bash -c "$JAVA_HOME/bin/java -Djava.net.preferIPv4Stack=true -Dhadoop.metrics.log.level=WARN   -Xmx820m -Djava.io.tmpdir=$PWD/tmp -Dlog4j.configuration=container-log4j.properties -Dyarn.app.container.log.dir=/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002 -Dyarn.app.container.log.filesize=0 -Dhadoop.root.logger=INFO,CLA -Dhadoop.root.logfile=syslog org.apache.hadoop.mapred.YarnChild 10.0.1.4 45261 attempt_1671326373437_0001_m_000000_0 2 1>/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/stdout 2>/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/stderr "

End of LogType:launch_container.sh
************************************************************************************

Container: container_1671326373437_0001_01_000002 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:prelaunch.err
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:0
LogContents:

End of LogType:prelaunch.err
******************************************************************************

Container: container_1671326373437_0001_01_000002 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:prelaunch.out
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:100
LogContents:
Setting up env variables
Setting up job resources
Copying debugging information
Launching container

End of LogType:prelaunch.out
******************************************************************************

Container: container_1671326373437_0001_01_000002 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:stderr
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:0
LogContents:

End of LogType:stderr
***********************************************************************

Container: container_1671326373437_0001_01_000002 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:stdout
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:0
LogContents:

End of LogType:stdout
***********************************************************************

Container: container_1671326373437_0001_01_000002 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:syslog
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:23202
LogContents:
2022-12-18 01:27:33,739 INFO [main] org.apache.hadoop.security.SecurityUtil: Updating Configuration
2022-12-18 01:27:33,782 INFO [main] org.apache.hadoop.metrics2.impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2022-12-18 01:27:33,823 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 second(s).
2022-12-18 01:27:33,823 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MapTask metrics system started
2022-12-18 01:27:33,850 INFO [main] org.apache.hadoop.mapred.YarnChild: Executing with tokens: [Kind: mapreduce.job, Service: job_1671326373437_0001, Ident: (org.apache.hadoop.mapreduce.security.token.JobTokenIdentifier@1ebd319f)]
2022-12-18 01:27:33,867 INFO [main] org.apache.hadoop.mapred.YarnChild: Sleeping for 0ms before retrying again. Got null now.
2022-12-18 01:27:33,975 INFO [main] org.apache.hadoop.mapred.YarnChild: mapreduce.cluster.local.dir for child: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001
2022-12-18 01:27:34,110 INFO [main] org.apache.hadoop.mapred.YarnChild: 
/************************************************************
[system properties]
os.name: Linux
os.version: 6.0.0-6-amd64
java.home: /opt/java/openjdk/jre
java.runtime.version: 1.8.0_345-b01
java.vendor: Temurin
java.version: 1.8.0_345
java.vm.name: OpenJDK 64-Bit Server VM
java.class.path: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000002:/hadoop/etc/hadoop:/hadoop/share/hadoop/common/hadoop-nfs-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-kms-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-registry-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-common-3.3.4-tests.jar:/hadoop/share/hadoop/common/hadoop-common-3.3.4.jar:/hadoop/share/hadoop/common/lib/kerby-pkix-1.0.1.jar:/hadoop/share/hadoop/common/lib/nimbus-jose-jwt-9.8.1.jar:/hadoop/share/hadoop/common/lib/jetty-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/asm-5.0.4.jar:/hadoop/share/hadoop/common/lib/paranamer-2.3.jar:/hadoop/share/hadoop/common/lib/commons-configuration2-2.1.1.jar:/hadoop/share/hadoop/common/lib/kerb-identity-1.0.1.jar:/hadoop/share/hadoop/common/lib/re2j-1.1.jar:/hadoop/share/hadoop/common/lib/jackson-xc-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-beanutils-1.9.4.jar:/hadoop/share/hadoop/common/lib/jsch-0.1.55.jar:/hadoop/share/hadoop/common/lib/commons-math3-3.1.1.jar:/hadoop/share/hadoop/common/lib/jackson-mapper-asl-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-security-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-codec-1.15.jar:/hadoop/share/hadoop/common/lib/gson-2.8.9.jar:/hadoop/share/hadoop/common/lib/j2objc-annotations-1.1.jar:/hadoop/share/hadoop/common/lib/jackson-core-asl-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-webapp-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/animal-sniffer-annotations-1.17.jar:/hadoop/share/hadoop/common/lib/jackson-jaxrs-1.9.13.jar:/hadoop/share/hadoop/common/lib/kerby-util-1.0.1.jar:/hadoop/share/hadoop/common/lib/zookeeper-3.5.6.jar:/hadoop/share/hadoop/common/lib/accessors-smart-2.4.7.jar:/hadoop/share/hadoop/common/lib/reload4j-1.2.22.jar:/hadoop/share/hadoop/common/lib/jcip-annotations-1.0-1.jar:/hadoop/share/hadoop/common/lib/jersey-servlet-1.19.jar:/hadoop/share/hadoop/common/lib/metrics-core-3.2.4.jar:/hadoop/share/hadoop/common/lib/jersey-json-1.19.jar:/hadoop/share/hadoop/common/lib/jsp-api-2.1.jar:/hadoop/share/hadoop/common/lib/curator-client-4.2.0.jar:/hadoop/share/hadoop/common/lib/curator-recipes-4.2.0.jar:/hadoop/share/hadoop/common/lib/commons-text-1.4.jar:/hadoop/share/hadoop/common/lib/jersey-server-1.19.jar:/hadoop/share/hadoop/common/lib/kerb-simplekdc-1.0.1.jar:/hadoop/share/hadoop/common/lib/jersey-core-1.19.jar:/hadoop/share/hadoop/common/lib/avro-1.7.7.jar:/hadoop/share/hadoop/common/lib/commons-io-2.8.0.jar:/hadoop/share/hadoop/common/lib/kerb-core-1.0.1.jar:/hadoop/share/hadoop/common/lib/slf4j-api-1.7.36.jar:/hadoop/share/hadoop/common/lib/kerb-server-1.0.1.jar:/hadoop/share/hadoop/common/lib/commons-collections-3.2.2.jar:/hadoop/share/hadoop/common/lib/jackson-core-2.12.7.jar:/hadoop/share/hadoop/common/lib/commons-daemon-1.0.13.jar:/hadoop/share/hadoop/common/lib/snappy-java-1.1.8.2.jar:/hadoop/share/hadoop/common/lib/jettison-1.1.jar:/hadoop/share/hadoop/common/lib/kerb-common-1.0.1.jar:/hadoop/share/hadoop/common/lib/jetty-http-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/failureaccess-1.0.jar:/hadoop/share/hadoop/common/lib/jul-to-slf4j-1.7.36.jar:/hadoop/share/hadoop/common/lib/jaxb-api-2.2.11.jar:/hadoop/share/hadoop/common/lib/jsr311-api-1.1.1.jar:/hadoop/share/hadoop/common/lib/jaxb-impl-2.2.3-1.jar:/hadoop/share/hadoop/common/lib/javax.servlet-api-3.1.0.jar:/hadoop/share/hadoop/common/lib/zookeeper-jute-3.5.6.jar:/hadoop/share/hadoop/common/lib/jetty-util-ajax-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-compress-1.21.jar:/hadoop/share/hadoop/common/lib/commons-net-3.6.jar:/hadoop/share/hadoop/common/lib/commons-cli-1.2.jar:/hadoop/share/hadoop/common/lib/checker-qual-2.5.2.jar:/hadoop/share/hadoop/common/lib/jetty-io-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/netty-3.10.6.Final.jar:/hadoop/share/hadoop/common/lib/kerb-crypto-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerby-asn1-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerby-xdr-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerb-util-1.0.1.jar:/hadoop/share/hadoop/common/lib/commons-logging-1.1.3.jar:/hadoop/share/hadoop/common/lib/commons-lang3-3.12.0.jar:/hadoop/share/hadoop/common/lib/token-provider-1.0.1.jar:/hadoop/share/hadoop/common/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/hadoop/share/hadoop/common/lib/jakarta.activation-api-1.2.1.jar:/hadoop/share/hadoop/common/lib/httpclient-4.5.13.jar:/hadoop/share/hadoop/common/lib/hadoop-shaded-guava-1.1.1.jar:/hadoop/share/hadoop/common/lib/hadoop-annotations-3.3.4.jar:/hadoop/share/hadoop/common/lib/hadoop-auth-3.3.4.jar:/hadoop/share/hadoop/common/lib/jackson-databind-2.12.7.jar:/hadoop/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar:/hadoop/share/hadoop/common/lib/curator-framework-4.2.0.jar:/hadoop/share/hadoop/common/lib/woodstox-core-5.3.0.jar:/hadoop/share/hadoop/common/lib/audience-annotations-0.5.0.jar:/hadoop/share/hadoop/common/lib/kerb-client-1.0.1.jar:/hadoop/share/hadoop/common/lib/json-smart-2.4.7.jar:/hadoop/share/hadoop/common/lib/dnsjava-2.1.7.jar:/hadoop/share/hadoop/common/lib/jsr305-3.0.2.jar:/hadoop/share/hadoop/common/lib/kerb-admin-1.0.1.jar:/hadoop/share/hadoop/common/lib/httpcore-4.4.13.jar:/hadoop/share/hadoop/common/lib/protobuf-java-2.5.0.jar:/hadoop/share/hadoop/common/lib/kerby-config-1.0.1.jar:/hadoop/share/hadoop/common/lib/jetty-util-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/jackson-annotations-2.12.7.jar:/hadoop/share/hadoop/common/lib/jetty-xml-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/hadoop-shaded-protobuf_3_7-1.1.1.jar:/hadoop/share/hadoop/common/lib/stax2-api-4.2.1.jar:/hadoop/share/hadoop/common/lib/guava-27.0-jre.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-native-client-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-rbf-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-rbf-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-native-client-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-httpfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-client-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-client-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-nfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/kerby-pkix-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/nimbus-jose-jwt-9.8.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/asm-5.0.4.jar:/hadoop/share/hadoop/hdfs/lib/paranamer-2.3.jar:/hadoop/share/hadoop/hdfs/lib/commons-configuration2-2.1.1.jar:/hadoop/share/hadoop/hdfs/lib/kerb-identity-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/re2j-1.1.jar:/hadoop/share/hadoop/hdfs/lib/jackson-xc-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/jetty-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-beanutils-1.9.4.jar:/hadoop/share/hadoop/hdfs/lib/leveldbjni-all-1.8.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-dns-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-rxtx-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jsch-0.1.55.jar:/hadoop/share/hadoop/hdfs/lib/commons-math3-3.1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-http2-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-udt-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jackson-mapper-asl-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/okhttp-4.9.3.jar:/hadoop/share/hadoop/hdfs/lib/jetty-security-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/commons-codec-1.15.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-mqtt-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-native-macos-4.1.77.Final-osx-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/gson-2.8.9.jar:/hadoop/share/hadoop/hdfs/lib/j2objc-annotations-1.1.jar:/hadoop/share/hadoop/hdfs/lib/jackson-core-asl-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/jetty-webapp-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/animal-sniffer-annotations-1.17.jar:/hadoop/share/hadoop/hdfs/lib/okio-2.8.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-handler-proxy-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jackson-jaxrs-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/kerby-util-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/zookeeper-3.5.6.jar:/hadoop/share/hadoop/hdfs/lib/accessors-smart-2.4.7.jar:/hadoop/share/hadoop/hdfs/lib/reload4j-1.2.22.jar:/hadoop/share/hadoop/hdfs/lib/jcip-annotations-1.0-1.jar:/hadoop/share/hadoop/hdfs/lib/jersey-servlet-1.19.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-kqueue-4.1.77.Final-osx-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/jersey-json-1.19.jar:/hadoop/share/hadoop/hdfs/lib/curator-client-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/curator-recipes-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/commons-text-1.4.jar:/hadoop/share/hadoop/hdfs/lib/kotlin-stdlib-common-1.4.10.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-unix-common-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-all-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-epoll-4.1.77.Final-linux-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/jersey-server-1.19.jar:/hadoop/share/hadoop/hdfs/lib/netty-common-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-simplekdc-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jersey-core-1.19.jar:/hadoop/share/hadoop/hdfs/lib/avro-1.7.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-io-2.8.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-haproxy-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-core-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-sctp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-server-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/commons-collections-3.2.2.jar:/hadoop/share/hadoop/hdfs/lib/jackson-core-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-http-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-daemon-1.0.13.jar:/hadoop/share/hadoop/hdfs/lib/snappy-java-1.1.8.2.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-classes-epoll-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jettison-1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-smtp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-common-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-http-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/failureaccess-1.0.jar:/hadoop/share/hadoop/hdfs/lib/kotlin-stdlib-1.4.10.jar:/hadoop/share/hadoop/hdfs/lib/jaxb-api-2.2.11.jar:/hadoop/share/hadoop/hdfs/lib/netty-buffer-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-classes-macos-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jsr311-api-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/json-simple-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-stomp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jaxb-impl-2.2.3-1.jar:/hadoop/share/hadoop/hdfs/lib/javax.servlet-api-3.1.0.jar:/hadoop/share/hadoop/hdfs/lib/zookeeper-jute-3.5.6.jar:/hadoop/share/hadoop/hdfs/lib/jetty-util-ajax-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-epoll-4.1.77.Final-linux-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/netty-handler-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-compress-1.21.jar:/hadoop/share/hadoop/hdfs/lib/commons-net-3.6.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-xml-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-cli-1.2.jar:/hadoop/share/hadoop/hdfs/lib/checker-qual-2.5.2.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-kqueue-4.1.77.Final-osx-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-memcache-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jetty-io-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-3.10.6.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-crypto-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerby-asn1-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerby-xdr-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerb-util-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/commons-logging-1.1.3.jar:/hadoop/share/hadoop/hdfs/lib/commons-lang3-3.12.0.jar:/hadoop/share/hadoop/hdfs/lib/token-provider-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/hadoop/share/hadoop/hdfs/lib/jakarta.activation-api-1.2.1.jar:/hadoop/share/hadoop/hdfs/lib/httpclient-4.5.13.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-redis-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-shaded-guava-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-annotations-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-auth-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/jackson-databind-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/curator-framework-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-native-macos-4.1.77.Final-osx-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/woodstox-core-5.3.0.jar:/hadoop/share/hadoop/hdfs/lib/audience-annotations-0.5.0.jar:/hadoop/share/hadoop/hdfs/lib/kerb-client-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/json-smart-2.4.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-socks-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-classes-kqueue-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/dnsjava-2.1.7.jar:/hadoop/share/hadoop/hdfs/lib/jsr305-3.0.2.jar:/hadoop/share/hadoop/hdfs/lib/kerb-admin-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/httpcore-4.4.13.jar:/hadoop/share/hadoop/hdfs/lib/protobuf-java-2.5.0.jar:/hadoop/share/hadoop/hdfs/lib/kerby-config-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-util-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/jackson-annotations-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/jetty-xml-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-shaded-protobuf_3_7-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/stax2-api-4.2.1.jar:/hadoop/share/hadoop/hdfs/lib/guava-27.0-jre.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-registry-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-router-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-client-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-distributedshell-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-services-core-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-nodemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-api-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-resourcemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-mawo-core-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-services-api-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-tests-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-unmanaged-am-launcher-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-sharedcachemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-web-proxy-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-timeline-pluginstorage-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-applicationhistoryservice-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-common-3.3.4.jar:/hadoop/share/hadoop/yarn/lib/javax.websocket-api-1.0.jar:/hadoop/share/hadoop/yarn/lib/websocket-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/json-io-2.5.1.jar:/hadoop/share/hadoop/yarn/lib/jline-3.9.0.jar:/hadoop/share/hadoop/yarn/lib/bcprov-jdk15on-1.60.jar:/hadoop/share/hadoop/yarn/lib/websocket-common-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jetty-jndi-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/websocket-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jackson-module-jaxb-annotations-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/HikariCP-java7-2.4.12.jar:/hadoop/share/hadoop/yarn/lib/jersey-client-1.19.jar:/hadoop/share/hadoop/yarn/lib/metrics-core-3.2.4.jar:/hadoop/share/hadoop/yarn/lib/jetty-client-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/guice-servlet-4.0.jar:/hadoop/share/hadoop/yarn/lib/swagger-annotations-1.5.4.jar:/hadoop/share/hadoop/yarn/lib/bcpkix-jdk15on-1.60.jar:/hadoop/share/hadoop/yarn/lib/websocket-api-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jna-5.2.0.jar:/hadoop/share/hadoop/yarn/lib/jackson-jaxrs-base-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/javax-websocket-client-impl-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/snakeyaml-1.26.jar:/hadoop/share/hadoop/yarn/lib/asm-tree-9.1.jar:/hadoop/share/hadoop/yarn/lib/javax.websocket-client-api-1.0.jar:/hadoop/share/hadoop/yarn/lib/javax-websocket-server-impl-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jackson-jaxrs-json-provider-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/asm-analysis-9.1.jar:/hadoop/share/hadoop/yarn/lib/websocket-client-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/ehcache-3.3.1.jar:/hadoop/share/hadoop/yarn/lib/guice-4.0.jar:/hadoop/share/hadoop/yarn/lib/fst-2.50.jar:/hadoop/share/hadoop/yarn/lib/jetty-plus-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jetty-annotations-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/geronimo-jcache_1.0_spec-1.0-alpha-1.jar:/hadoop/share/hadoop/yarn/lib/mssql-jdbc-6.2.1.jre7.jar:/hadoop/share/hadoop/yarn/lib/objenesis-2.6.jar:/hadoop/share/hadoop/yarn/lib/jersey-guice-1.19.jar:/hadoop/share/hadoop/yarn/lib/jakarta.xml.bind-api-2.3.2.jar:/hadoop/share/hadoop/yarn/lib/aopalliance-1.0.jar:/hadoop/share/hadoop/yarn/lib/javax.inject-1.jar:/hadoop/share/hadoop/yarn/lib/asm-commons-9.1.jar:/hadoop/share/hadoop/yarn/lib/java-util-1.9.0.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-plugins-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-shuffle-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.4-tests.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-nativetask-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-app-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-uploader-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.3.4.jar:/hadoop/share/hadoop/mapreduce/lib/*:job.jar/job.jar:job.jar/classes/:job.jar/lib/*:/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000002/job.jar
java.io.tmpdir: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000002/tmp
user.dir: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000002
user.name: yarn
************************************************************/
2022-12-18 01:27:34,110 INFO [main] org.apache.hadoop.conf.Configuration.deprecation: session.id is deprecated. Instead, use dfs.metrics.session-id
2022-12-18 01:27:34,336 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: File Output Committer Algorithm version is 2
2022-12-18 01:27:34,336 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2022-12-18 01:27:34,344 INFO [main] org.apache.hadoop.mapred.Task:  Using ResourceCalculatorProcessTree : [ ]
2022-12-18 01:27:34,421 INFO [main] org.apache.hadoop.mapred.MapTask: Processing split: org.apache.hadoop.examples.terasort.TeraGen$RangeInputFormat$RangeInputSplit@46f699d5
2022-12-18 01:27:34,828 INFO [main] org.apache.hadoop.mapred.Task: Task:attempt_1671326373437_0001_m_000000_0 is done. And is in the process of committing
2022-12-18 01:27:34,835 INFO [main] org.apache.hadoop.mapred.Task: Task attempt_1671326373437_0001_m_000000_0 is allowed to commit now
2022-12-18 01:27:34,853 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: Saved output of task 'attempt_1671326373437_0001_m_000000_0' to hdfs://namenode:8020/user/sandbox/teragen
2022-12-18 01:27:34,864 INFO [main] org.apache.hadoop.mapred.Task: Task 'attempt_1671326373437_0001_m_000000_0' done.
2022-12-18 01:27:34,868 INFO [main] org.apache.hadoop.mapred.Task: Final Counters for attempt_1671326373437_0001_m_000000_0: Counters: 27
	File System Counters
		FILE: Number of bytes read=0
		FILE: Number of bytes written=275762
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=82
		HDFS: Number of bytes written=50000000
		HDFS: Number of read operations=6
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Map-Reduce Framework
		Map input records=500000
		Map output records=500000
		Input split bytes=82
		Spilled Records=0
		Failed Shuffles=0
		Merged Map outputs=0
		GC time elapsed (ms)=31
		CPU time spent (ms)=1650
		Physical memory (bytes) snapshot=384585728
		Virtual memory (bytes) snapshot=2617733120
		Total committed heap usage (bytes)=603979776
		Peak Map Physical memory (bytes)=384585728
		Peak Map Virtual memory (bytes)=2617733120
	org.apache.hadoop.examples.terasort.TeraGen$Counters
		CHECKSUM=1074598070305752
	File Input Format Counters 
		Bytes Read=0
	File Output Format Counters 
		Bytes Written=50000000
2022-12-18 01:27:34,869 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: Stopping MapTask metrics system...
2022-12-18 01:27:34,869 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MapTask metrics system stopped.
2022-12-18 01:27:34,869 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MapTask metrics system shutdown complete.

End of LogType:syslog
***********************************************************************

Container: container_1671326373437_0001_01_000001 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:directory.info
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:2280
LogContents:
ls -l:
total 36
-rw-r--r-- 1 yarn yarn  105 Dec 18 01:27 container_tokens
-rwx------ 1 yarn yarn  627 Dec 18 01:27 default_container_executor_session.sh
-rwx------ 1 yarn yarn  682 Dec 18 01:27 default_container_executor.sh
lrwxrwxrwx 1 yarn yarn   97 Dec 18 01:27 job.jar -> /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/11/job.jar
drwxr-xr-x 2 yarn yarn 4096 Dec 18 01:27 jobSubmitDir
lrwxrwxrwx 1 yarn yarn   97 Dec 18 01:27 job.xml -> /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/13/job.xml
-rwx------ 1 yarn yarn 4954 Dec 18 01:27 launch_container.sh
drwx--x--- 2 yarn yarn 4096 Dec 18 01:27 tmp
find -L . -maxdepth 5 -ls:
 63318123      4 drwx--x---   4 yarn     yarn         4096 Dec 18 01:27 .
 63318125      4 drwx--x---   2 yarn     yarn         4096 Dec 18 01:27 ./tmp
 63318132      4 -rwx------   1 yarn     yarn          682 Dec 18 01:27 ./default_container_executor.sh
 63318130      4 -rwx------   1 yarn     yarn          627 Dec 18 01:27 ./default_container_executor_session.sh
 63318129      4 -rw-r--r--   1 yarn     yarn           48 Dec 18 01:27 ./.launch_container.sh.crc
 63317898      4 drwx------   2 yarn     yarn         4096 Dec 18 01:27 ./job.jar
 63317919    276 -r-x------   1 yarn     yarn       280992 Dec 18 01:27 ./job.jar/job.jar
 63318131      4 -rw-r--r--   1 yarn     yarn           16 Dec 18 01:27 ./.default_container_executor_session.sh.crc
 63318115    232 -r-x------   1 yarn     yarn       235968 Dec 18 01:27 ./job.xml
 63318126      4 -rw-r--r--   1 yarn     yarn          105 Dec 18 01:27 ./container_tokens
 63318138      4 drwxr-xr-x   2 yarn     yarn         4096 Dec 18 01:27 ./jobSubmitDir
 63318112      4 -r-x------   1 yarn     yarn          174 Dec 18 01:27 ./jobSubmitDir/job.split
 63318105      4 -r-x------   1 yarn     yarn           16 Dec 18 01:27 ./jobSubmitDir/job.splitmetainfo
 63318128      8 -rwx------   1 yarn     yarn         4954 Dec 18 01:27 ./launch_container.sh
 63318127      4 -rw-r--r--   1 yarn     yarn           12 Dec 18 01:27 ./.container_tokens.crc
 63318133      4 -rw-r--r--   1 yarn     yarn           16 Dec 18 01:27 ./.default_container_executor.sh.crc
broken symlinks(find -L . -maxdepth 5 -type l -ls):

End of LogType:directory.info
*******************************************************************************

Container: container_1671326373437_0001_01_000001 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:launch_container.sh
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:4954
LogContents:
#!/bin/bash

set -o pipefail -e
export PRELAUNCH_OUT="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/prelaunch.out"
exec >"${PRELAUNCH_OUT}"
export PRELAUNCH_ERR="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/prelaunch.err"
exec 2>"${PRELAUNCH_ERR}"
echo "Setting up env variables"
export JAVA_HOME=${JAVA_HOME:-"/opt/java/openjdk"}
export HADOOP_COMMON_HOME=${HADOOP_COMMON_HOME:-"/hadoop"}
export HADOOP_HDFS_HOME=${HADOOP_HDFS_HOME:-"/hadoop"}
export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/hadoop/etc/hadoop"}
export HADOOP_YARN_HOME=${HADOOP_YARN_HOME:-"/hadoop"}
export HADOOP_HOME=${HADOOP_HOME:-"/hadoop"}
export PATH=${PATH:-"/hadoop/bin:/hadoop/sbin:/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"}
export LANG=${LANG:-"en_US.UTF-8"}
export HADOOP_MAPRED_HOME=${HADOOP_MAPRED_HOME:-"/hadoop"}
export HADOOP_TOKEN_FILE_LOCATION="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001/container_tokens"
export CONTAINER_ID="container_1671326373437_0001_01_000001"
export NM_PORT="36113"
export NM_HOST="hadoopnode"
export NM_HTTP_PORT="8042"
export LOCAL_DIRS="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001"
export LOCAL_USER_DIRS="/data/nm-local-dir/usercache/sandbox/"
export LOG_DIRS="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001"
export USER="sandbox"
export LOGNAME="sandbox"
export HOME="/home/"
export PWD="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001"
export LOCALIZATION_COUNTERS="519026,0,4,0,296"
export JVM_PID="$$"
export NM_AUX_SERVICE_mapreduce_shuffle="AAA0+gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
export APPLICATION_WEB_PROXY_BASE="/proxy/application_1671326373437_0001"
export SHELL="/bin/bash"
export CLASSPATH="$PWD:$HADOOP_CONF_DIR:$HADOOP_COMMON_HOME/share/hadoop/common/*:$HADOOP_COMMON_HOME/share/hadoop/common/lib/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/lib/*:$HADOOP_YARN_HOME/share/hadoop/yarn/*:$HADOOP_YARN_HOME/share/hadoop/yarn/lib/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*:job.jar/*:job.jar/classes/:job.jar/lib/*:$PWD/*"
export APP_SUBMIT_TIME_ENV="1671326847669"
export LD_LIBRARY_PATH="$PWD:$HADOOP_COMMON_HOME/lib/native"
export MALLOC_ARENA_MAX="4"
echo "Setting up job resources"
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/11/job.jar" "job.jar"
mkdir -p jobSubmitDir
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/10/job.splitmetainfo" "jobSubmitDir/job.splitmetainfo"
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/13/job.xml" "job.xml"
mkdir -p jobSubmitDir
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/12/job.split" "jobSubmitDir/job.split"
echo "Copying debugging information"
# Creating copy of launch script
cp "launch_container.sh" "/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/launch_container.sh"
chmod 640 "/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/launch_container.sh"
# Determining directory contents
echo "ls -l:" 1>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/directory.info"
ls -l 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/directory.info"
echo "find -L . -maxdepth 5 -ls:" 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/directory.info"
find -L . -maxdepth 5 -ls 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/directory.info"
echo "broken symlinks(find -L . -maxdepth 5 -type l -ls):" 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/directory.info"
find -L . -maxdepth 5 -type l -ls 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/directory.info"
echo "Launching container"
exec /bin/bash -c "$JAVA_HOME/bin/java -Djava.io.tmpdir=$PWD/tmp -Dlog4j.configuration=container-log4j.properties -Dyarn.app.container.log.dir=/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001 -Dyarn.app.container.log.filesize=0 -Dhadoop.root.logger=INFO,CLA -Dhadoop.root.logfile=syslog  -Xmx1024m org.apache.hadoop.mapreduce.v2.app.MRAppMaster 1>/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/stdout 2>/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/stderr "

End of LogType:launch_container.sh
************************************************************************************

Container: container_1671326373437_0001_01_000001 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:prelaunch.err
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:0
LogContents:

End of LogType:prelaunch.err
******************************************************************************

Container: container_1671326373437_0001_01_000001 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:prelaunch.out
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:100
LogContents:
Setting up env variables
Setting up job resources
Copying debugging information
Launching container

End of LogType:prelaunch.out
******************************************************************************

Container: container_1671326373437_0001_01_000001 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:stderr
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:1722
LogContents:
Dec 18, 2022 1:27:30 AM com.sun.jersey.guice.spi.container.GuiceComponentProviderFactory register
INFO: Registering org.apache.hadoop.mapreduce.v2.app.webapp.JAXBContextResolver as a provider class
Dec 18, 2022 1:27:30 AM com.sun.jersey.guice.spi.container.GuiceComponentProviderFactory register
INFO: Registering org.apache.hadoop.yarn.webapp.GenericExceptionHandler as a provider class
Dec 18, 2022 1:27:30 AM com.sun.jersey.guice.spi.container.GuiceComponentProviderFactory register
INFO: Registering org.apache.hadoop.mapreduce.v2.app.webapp.AMWebServices as a root resource class
Dec 18, 2022 1:27:30 AM com.sun.jersey.server.impl.application.WebApplicationImpl _initiate
INFO: Initiating Jersey application, version 'Jersey: 1.19 02/11/2015 03:25 AM'
Dec 18, 2022 1:27:30 AM com.sun.jersey.guice.spi.container.GuiceComponentProviderFactory getComponentProvider
INFO: Binding org.apache.hadoop.mapreduce.v2.app.webapp.JAXBContextResolver to GuiceManagedComponentProvider with the scope "Singleton"
Dec 18, 2022 1:27:30 AM com.sun.jersey.guice.spi.container.GuiceComponentProviderFactory getComponentProvider
INFO: Binding org.apache.hadoop.yarn.webapp.GenericExceptionHandler to GuiceManagedComponentProvider with the scope "Singleton"
Dec 18, 2022 1:27:30 AM com.sun.jersey.guice.spi.container.GuiceComponentProviderFactory getComponentProvider
INFO: Binding org.apache.hadoop.mapreduce.v2.app.webapp.AMWebServices to GuiceManagedComponentProvider with the scope "PerRequest"
log4j:WARN No appenders could be found for logger (org.apache.hadoop.mapreduce.v2.app.MRAppMaster).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.

End of LogType:stderr
***********************************************************************

Container: container_1671326373437_0001_01_000001 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:stdout
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:0
LogContents:

End of LogType:stdout
***********************************************************************

Container: container_1671326373437_0001_01_000001 on hadoopnode_36113
LogAggregationType: AGGREGATED
=====================================================================
LogType:syslog
LogLastModifiedTime:Sun Dec 18 01:27:43 +0000 2022
LogLength:55584
LogContents:
2022-12-18 01:27:29,315 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Created MRAppMaster for application appattempt_1671326373437_0001_000001
2022-12-18 01:27:29,366 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: 
/************************************************************
[system properties]
os.name: Linux
os.version: 6.0.0-6-amd64
java.home: /opt/java/openjdk/jre
java.runtime.version: 1.8.0_345-b01
java.vendor: Temurin
java.version: 1.8.0_345
java.vm.name: OpenJDK 64-Bit Server VM
java.class.path: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001:/hadoop/etc/hadoop:/hadoop/share/hadoop/common/hadoop-nfs-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-kms-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-registry-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-common-3.3.4-tests.jar:/hadoop/share/hadoop/common/hadoop-common-3.3.4.jar:/hadoop/share/hadoop/common/lib/kerby-pkix-1.0.1.jar:/hadoop/share/hadoop/common/lib/nimbus-jose-jwt-9.8.1.jar:/hadoop/share/hadoop/common/lib/jetty-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/asm-5.0.4.jar:/hadoop/share/hadoop/common/lib/paranamer-2.3.jar:/hadoop/share/hadoop/common/lib/commons-configuration2-2.1.1.jar:/hadoop/share/hadoop/common/lib/kerb-identity-1.0.1.jar:/hadoop/share/hadoop/common/lib/re2j-1.1.jar:/hadoop/share/hadoop/common/lib/jackson-xc-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-beanutils-1.9.4.jar:/hadoop/share/hadoop/common/lib/jsch-0.1.55.jar:/hadoop/share/hadoop/common/lib/commons-math3-3.1.1.jar:/hadoop/share/hadoop/common/lib/jackson-mapper-asl-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-security-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-codec-1.15.jar:/hadoop/share/hadoop/common/lib/gson-2.8.9.jar:/hadoop/share/hadoop/common/lib/j2objc-annotations-1.1.jar:/hadoop/share/hadoop/common/lib/jackson-core-asl-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-webapp-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/animal-sniffer-annotations-1.17.jar:/hadoop/share/hadoop/common/lib/jackson-jaxrs-1.9.13.jar:/hadoop/share/hadoop/common/lib/kerby-util-1.0.1.jar:/hadoop/share/hadoop/common/lib/zookeeper-3.5.6.jar:/hadoop/share/hadoop/common/lib/accessors-smart-2.4.7.jar:/hadoop/share/hadoop/common/lib/reload4j-1.2.22.jar:/hadoop/share/hadoop/common/lib/jcip-annotations-1.0-1.jar:/hadoop/share/hadoop/common/lib/jersey-servlet-1.19.jar:/hadoop/share/hadoop/common/lib/metrics-core-3.2.4.jar:/hadoop/share/hadoop/common/lib/jersey-json-1.19.jar:/hadoop/share/hadoop/common/lib/jsp-api-2.1.jar:/hadoop/share/hadoop/common/lib/curator-client-4.2.0.jar:/hadoop/share/hadoop/common/lib/curator-recipes-4.2.0.jar:/hadoop/share/hadoop/common/lib/commons-text-1.4.jar:/hadoop/share/hadoop/common/lib/jersey-server-1.19.jar:/hadoop/share/hadoop/common/lib/kerb-simplekdc-1.0.1.jar:/hadoop/share/hadoop/common/lib/jersey-core-1.19.jar:/hadoop/share/hadoop/common/lib/avro-1.7.7.jar:/hadoop/share/hadoop/common/lib/commons-io-2.8.0.jar:/hadoop/share/hadoop/common/lib/kerb-core-1.0.1.jar:/hadoop/share/hadoop/common/lib/slf4j-api-1.7.36.jar:/hadoop/share/hadoop/common/lib/kerb-server-1.0.1.jar:/hadoop/share/hadoop/common/lib/commons-collections-3.2.2.jar:/hadoop/share/hadoop/common/lib/jackson-core-2.12.7.jar:/hadoop/share/hadoop/common/lib/commons-daemon-1.0.13.jar:/hadoop/share/hadoop/common/lib/snappy-java-1.1.8.2.jar:/hadoop/share/hadoop/common/lib/jettison-1.1.jar:/hadoop/share/hadoop/common/lib/kerb-common-1.0.1.jar:/hadoop/share/hadoop/common/lib/jetty-http-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/failureaccess-1.0.jar:/hadoop/share/hadoop/common/lib/jul-to-slf4j-1.7.36.jar:/hadoop/share/hadoop/common/lib/jaxb-api-2.2.11.jar:/hadoop/share/hadoop/common/lib/jsr311-api-1.1.1.jar:/hadoop/share/hadoop/common/lib/jaxb-impl-2.2.3-1.jar:/hadoop/share/hadoop/common/lib/javax.servlet-api-3.1.0.jar:/hadoop/share/hadoop/common/lib/zookeeper-jute-3.5.6.jar:/hadoop/share/hadoop/common/lib/jetty-util-ajax-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-compress-1.21.jar:/hadoop/share/hadoop/common/lib/commons-net-3.6.jar:/hadoop/share/hadoop/common/lib/commons-cli-1.2.jar:/hadoop/share/hadoop/common/lib/checker-qual-2.5.2.jar:/hadoop/share/hadoop/common/lib/jetty-io-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/netty-3.10.6.Final.jar:/hadoop/share/hadoop/common/lib/kerb-crypto-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerby-asn1-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerby-xdr-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerb-util-1.0.1.jar:/hadoop/share/hadoop/common/lib/commons-logging-1.1.3.jar:/hadoop/share/hadoop/common/lib/commons-lang3-3.12.0.jar:/hadoop/share/hadoop/common/lib/token-provider-1.0.1.jar:/hadoop/share/hadoop/common/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/hadoop/share/hadoop/common/lib/jakarta.activation-api-1.2.1.jar:/hadoop/share/hadoop/common/lib/httpclient-4.5.13.jar:/hadoop/share/hadoop/common/lib/hadoop-shaded-guava-1.1.1.jar:/hadoop/share/hadoop/common/lib/hadoop-annotations-3.3.4.jar:/hadoop/share/hadoop/common/lib/hadoop-auth-3.3.4.jar:/hadoop/share/hadoop/common/lib/jackson-databind-2.12.7.jar:/hadoop/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar:/hadoop/share/hadoop/common/lib/curator-framework-4.2.0.jar:/hadoop/share/hadoop/common/lib/woodstox-core-5.3.0.jar:/hadoop/share/hadoop/common/lib/audience-annotations-0.5.0.jar:/hadoop/share/hadoop/common/lib/kerb-client-1.0.1.jar:/hadoop/share/hadoop/common/lib/json-smart-2.4.7.jar:/hadoop/share/hadoop/common/lib/dnsjava-2.1.7.jar:/hadoop/share/hadoop/common/lib/jsr305-3.0.2.jar:/hadoop/share/hadoop/common/lib/kerb-admin-1.0.1.jar:/hadoop/share/hadoop/common/lib/httpcore-4.4.13.jar:/hadoop/share/hadoop/common/lib/protobuf-java-2.5.0.jar:/hadoop/share/hadoop/common/lib/kerby-config-1.0.1.jar:/hadoop/share/hadoop/common/lib/jetty-util-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/jackson-annotations-2.12.7.jar:/hadoop/share/hadoop/common/lib/jetty-xml-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/hadoop-shaded-protobuf_3_7-1.1.1.jar:/hadoop/share/hadoop/common/lib/stax2-api-4.2.1.jar:/hadoop/share/hadoop/common/lib/guava-27.0-jre.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-native-client-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-rbf-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-rbf-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-native-client-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-httpfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-client-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-client-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-nfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/kerby-pkix-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/nimbus-jose-jwt-9.8.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/asm-5.0.4.jar:/hadoop/share/hadoop/hdfs/lib/paranamer-2.3.jar:/hadoop/share/hadoop/hdfs/lib/commons-configuration2-2.1.1.jar:/hadoop/share/hadoop/hdfs/lib/kerb-identity-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/re2j-1.1.jar:/hadoop/share/hadoop/hdfs/lib/jackson-xc-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/jetty-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-beanutils-1.9.4.jar:/hadoop/share/hadoop/hdfs/lib/leveldbjni-all-1.8.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-dns-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-rxtx-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jsch-0.1.55.jar:/hadoop/share/hadoop/hdfs/lib/commons-math3-3.1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-http2-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-udt-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jackson-mapper-asl-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/okhttp-4.9.3.jar:/hadoop/share/hadoop/hdfs/lib/jetty-security-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/commons-codec-1.15.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-mqtt-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-native-macos-4.1.77.Final-osx-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/gson-2.8.9.jar:/hadoop/share/hadoop/hdfs/lib/j2objc-annotations-1.1.jar:/hadoop/share/hadoop/hdfs/lib/jackson-core-asl-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/jetty-webapp-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/animal-sniffer-annotations-1.17.jar:/hadoop/share/hadoop/hdfs/lib/okio-2.8.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-handler-proxy-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jackson-jaxrs-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/kerby-util-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/zookeeper-3.5.6.jar:/hadoop/share/hadoop/hdfs/lib/accessors-smart-2.4.7.jar:/hadoop/share/hadoop/hdfs/lib/reload4j-1.2.22.jar:/hadoop/share/hadoop/hdfs/lib/jcip-annotations-1.0-1.jar:/hadoop/share/hadoop/hdfs/lib/jersey-servlet-1.19.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-kqueue-4.1.77.Final-osx-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/jersey-json-1.19.jar:/hadoop/share/hadoop/hdfs/lib/curator-client-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/curator-recipes-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/commons-text-1.4.jar:/hadoop/share/hadoop/hdfs/lib/kotlin-stdlib-common-1.4.10.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-unix-common-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-all-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-epoll-4.1.77.Final-linux-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/jersey-server-1.19.jar:/hadoop/share/hadoop/hdfs/lib/netty-common-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-simplekdc-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jersey-core-1.19.jar:/hadoop/share/hadoop/hdfs/lib/avro-1.7.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-io-2.8.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-haproxy-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-core-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-sctp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-server-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/commons-collections-3.2.2.jar:/hadoop/share/hadoop/hdfs/lib/jackson-core-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-http-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-daemon-1.0.13.jar:/hadoop/share/hadoop/hdfs/lib/snappy-java-1.1.8.2.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-classes-epoll-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jettison-1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-smtp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-common-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-http-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/failureaccess-1.0.jar:/hadoop/share/hadoop/hdfs/lib/kotlin-stdlib-1.4.10.jar:/hadoop/share/hadoop/hdfs/lib/jaxb-api-2.2.11.jar:/hadoop/share/hadoop/hdfs/lib/netty-buffer-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-classes-macos-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jsr311-api-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/json-simple-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-stomp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jaxb-impl-2.2.3-1.jar:/hadoop/share/hadoop/hdfs/lib/javax.servlet-api-3.1.0.jar:/hadoop/share/hadoop/hdfs/lib/zookeeper-jute-3.5.6.jar:/hadoop/share/hadoop/hdfs/lib/jetty-util-ajax-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-epoll-4.1.77.Final-linux-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/netty-handler-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-compress-1.21.jar:/hadoop/share/hadoop/hdfs/lib/commons-net-3.6.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-xml-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-cli-1.2.jar:/hadoop/share/hadoop/hdfs/lib/checker-qual-2.5.2.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-kqueue-4.1.77.Final-osx-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-memcache-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jetty-io-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-3.10.6.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-crypto-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerby-asn1-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerby-xdr-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerb-util-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/commons-logging-1.1.3.jar:/hadoop/share/hadoop/hdfs/lib/commons-lang3-3.12.0.jar:/hadoop/share/hadoop/hdfs/lib/token-provider-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/hadoop/share/hadoop/hdfs/lib/jakarta.activation-api-1.2.1.jar:/hadoop/share/hadoop/hdfs/lib/httpclient-4.5.13.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-redis-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-shaded-guava-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-annotations-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-auth-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/jackson-databind-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/curator-framework-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-native-macos-4.1.77.Final-osx-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/woodstox-core-5.3.0.jar:/hadoop/share/hadoop/hdfs/lib/audience-annotations-0.5.0.jar:/hadoop/share/hadoop/hdfs/lib/kerb-client-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/json-smart-2.4.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-socks-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-classes-kqueue-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/dnsjava-2.1.7.jar:/hadoop/share/hadoop/hdfs/lib/jsr305-3.0.2.jar:/hadoop/share/hadoop/hdfs/lib/kerb-admin-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/httpcore-4.4.13.jar:/hadoop/share/hadoop/hdfs/lib/protobuf-java-2.5.0.jar:/hadoop/share/hadoop/hdfs/lib/kerby-config-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-util-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/jackson-annotations-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/jetty-xml-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-shaded-protobuf_3_7-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/stax2-api-4.2.1.jar:/hadoop/share/hadoop/hdfs/lib/guava-27.0-jre.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-registry-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-router-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-client-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-distributedshell-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-services-core-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-nodemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-api-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-resourcemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-mawo-core-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-services-api-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-tests-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-unmanaged-am-launcher-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-sharedcachemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-web-proxy-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-timeline-pluginstorage-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-applicationhistoryservice-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-common-3.3.4.jar:/hadoop/share/hadoop/yarn/lib/javax.websocket-api-1.0.jar:/hadoop/share/hadoop/yarn/lib/websocket-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/json-io-2.5.1.jar:/hadoop/share/hadoop/yarn/lib/jline-3.9.0.jar:/hadoop/share/hadoop/yarn/lib/bcprov-jdk15on-1.60.jar:/hadoop/share/hadoop/yarn/lib/websocket-common-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jetty-jndi-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/websocket-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jackson-module-jaxb-annotations-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/HikariCP-java7-2.4.12.jar:/hadoop/share/hadoop/yarn/lib/jersey-client-1.19.jar:/hadoop/share/hadoop/yarn/lib/metrics-core-3.2.4.jar:/hadoop/share/hadoop/yarn/lib/jetty-client-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/guice-servlet-4.0.jar:/hadoop/share/hadoop/yarn/lib/swagger-annotations-1.5.4.jar:/hadoop/share/hadoop/yarn/lib/bcpkix-jdk15on-1.60.jar:/hadoop/share/hadoop/yarn/lib/websocket-api-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jna-5.2.0.jar:/hadoop/share/hadoop/yarn/lib/jackson-jaxrs-base-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/javax-websocket-client-impl-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/snakeyaml-1.26.jar:/hadoop/share/hadoop/yarn/lib/asm-tree-9.1.jar:/hadoop/share/hadoop/yarn/lib/javax.websocket-client-api-1.0.jar:/hadoop/share/hadoop/yarn/lib/javax-websocket-server-impl-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jackson-jaxrs-json-provider-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/asm-analysis-9.1.jar:/hadoop/share/hadoop/yarn/lib/websocket-client-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/ehcache-3.3.1.jar:/hadoop/share/hadoop/yarn/lib/guice-4.0.jar:/hadoop/share/hadoop/yarn/lib/fst-2.50.jar:/hadoop/share/hadoop/yarn/lib/jetty-plus-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jetty-annotations-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/geronimo-jcache_1.0_spec-1.0-alpha-1.jar:/hadoop/share/hadoop/yarn/lib/mssql-jdbc-6.2.1.jre7.jar:/hadoop/share/hadoop/yarn/lib/objenesis-2.6.jar:/hadoop/share/hadoop/yarn/lib/jersey-guice-1.19.jar:/hadoop/share/hadoop/yarn/lib/jakarta.xml.bind-api-2.3.2.jar:/hadoop/share/hadoop/yarn/lib/aopalliance-1.0.jar:/hadoop/share/hadoop/yarn/lib/javax.inject-1.jar:/hadoop/share/hadoop/yarn/lib/asm-commons-9.1.jar:/hadoop/share/hadoop/yarn/lib/java-util-1.9.0.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-plugins-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-shuffle-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.4-tests.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-nativetask-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-app-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-uploader-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.3.4.jar:/hadoop/share/hadoop/mapreduce/lib/*:job.jar/job.jar:job.jar/classes/:job.jar/lib/*:/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001/job.jar
java.io.tmpdir: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001/tmp
user.dir: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001
user.name: yarn
************************************************************/
2022-12-18 01:27:29,393 INFO [main] org.apache.hadoop.security.SecurityUtil: Updating Configuration
2022-12-18 01:27:29,453 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Executing with tokens: [Kind: YARN_AM_RM_TOKEN, Service: , Ident: (appAttemptId { application_id { id: 1 cluster_timestamp: 1671326373437 } attemptId: 1 } keyId: -928306625)]
2022-12-18 01:27:29,471 INFO [main] org.apache.hadoop.conf.Configuration: resource-types.xml not found
2022-12-18 01:27:29,472 INFO [main] org.apache.hadoop.yarn.util.resource.ResourceUtils: Unable to find 'resource-types.xml'.
2022-12-18 01:27:29,478 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Using mapred newApiCommitter.
2022-12-18 01:27:29,479 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: OutputCommitter set in config null
2022-12-18 01:27:29,497 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: File Output Committer Algorithm version is 2
2022-12-18 01:27:29,497 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2022-12-18 01:27:29,739 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: OutputCommitter is org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter
2022-12-18 01:27:29,796 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.jobhistory.EventType for class org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler
2022-12-18 01:27:29,797 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.job.event.JobEventType for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$JobEventDispatcher
2022-12-18 01:27:29,797 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.job.event.TaskEventType for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$TaskEventDispatcher
2022-12-18 01:27:29,797 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.job.event.TaskAttemptEventType for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$TaskAttemptEventDispatcher
2022-12-18 01:27:29,798 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.commit.CommitterEventType for class org.apache.hadoop.mapreduce.v2.app.commit.CommitterEventHandler
2022-12-18 01:27:29,800 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.speculate.Speculator$EventType for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$SpeculatorEventDispatcher
2022-12-18 01:27:29,800 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.rm.ContainerAllocator$EventType for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$ContainerAllocatorRouter
2022-12-18 01:27:29,801 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncher$EventType for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$ContainerLauncherRouter
2022-12-18 01:27:29,813 INFO [main] org.apache.hadoop.mapreduce.v2.jobhistory.JobHistoryUtils: Default file system [hdfs://namenode:8020]
2022-12-18 01:27:29,820 INFO [main] org.apache.hadoop.mapreduce.v2.jobhistory.JobHistoryUtils: Default file system [hdfs://namenode:8020]
2022-12-18 01:27:29,826 INFO [main] org.apache.hadoop.mapreduce.v2.jobhistory.JobHistoryUtils: Default file system [hdfs://namenode:8020]
2022-12-18 01:27:29,839 INFO [main] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Perms after creating 488, Expected: 504
2022-12-18 01:27:29,839 INFO [main] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Explicitly setting permissions to : 504, rwxrwx---
2022-12-18 01:27:29,842 INFO [main] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Emitting job history data to the timeline server is not enabled
2022-12-18 01:27:29,863 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.job.event.JobFinishEvent$Type for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$JobFinishEventHandler
2022-12-18 01:27:29,946 INFO [main] org.apache.hadoop.metrics2.impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2022-12-18 01:27:29,977 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 second(s).
2022-12-18 01:27:29,977 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MRAppMaster metrics system started
2022-12-18 01:27:29,981 INFO [main] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Adding job token for job_1671326373437_0001 to jobTokenSecretManager
2022-12-18 01:27:30,079 INFO [main] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Not uberizing job_1671326373437_0001 because: not enabled;
2022-12-18 01:27:30,094 INFO [main] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Input size for job job_1671326373437_0001 = 0. Number of splits = 2
2022-12-18 01:27:30,094 INFO [main] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Number of reduces for job job_1671326373437_0001 = 0
2022-12-18 01:27:30,094 INFO [main] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: job_1671326373437_0001Job Transitioned from NEW to INITED
2022-12-18 01:27:30,095 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: MRAppMaster launching normal, non-uberized, multi-container job job_1671326373437_0001.
2022-12-18 01:27:30,122 INFO [main] org.apache.hadoop.ipc.CallQueueManager: Using callQueue: class java.util.concurrent.LinkedBlockingQueue, queueCapacity: 100, scheduler: class org.apache.hadoop.ipc.DefaultRpcScheduler, ipcBackoff: false.
2022-12-18 01:27:30,130 INFO [Socket Reader #1 for port 0] org.apache.hadoop.ipc.Server: Starting Socket Reader #1 for port 0
2022-12-18 01:27:30,241 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.yarn.factories.impl.pb.RpcServerFactoryPBImpl: Adding protocol org.apache.hadoop.mapreduce.v2.api.MRClientProtocolPB to the server
2022-12-18 01:27:30,241 INFO [IPC Server listener on 0] org.apache.hadoop.ipc.Server: IPC Server listener on 0: starting
2022-12-18 01:27:30,241 INFO [IPC Server Responder] org.apache.hadoop.ipc.Server: IPC Server Responder: starting
2022-12-18 01:27:30,242 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.mapreduce.v2.app.client.MRClientService: Instantiated MRClientService at hadoopnode/10.0.1.4:39881
2022-12-18 01:27:30,257 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.util.log: Logging initialized @1359ms to org.eclipse.jetty.util.log.Slf4jLog
2022-12-18 01:27:30,328 WARN [Listener at 0.0.0.0/39881] org.apache.hadoop.security.authentication.server.AuthenticationFilter: Unable to initialize FileSignerSecretProvider, falling back to use random secrets. Reason: Could not read signature secret file: //hadoop-http-auth-signature-secret
2022-12-18 01:27:30,330 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.http.HttpRequestLog: Http request log for http.requests.mapreduce is not defined
2022-12-18 01:27:30,333 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.http.HttpServer2: Added global filter 'safety' (class=org.apache.hadoop.http.HttpServer2$QuotingInputFilter)
2022-12-18 01:27:30,346 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.http.HttpServer2: Added filter AM_PROXY_FILTER (class=org.apache.hadoop.yarn.server.webproxy.amfilter.AmIpFilter) to context mapreduce
2022-12-18 01:27:30,346 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.http.HttpServer2: Added filter AM_PROXY_FILTER (class=org.apache.hadoop.yarn.server.webproxy.amfilter.AmIpFilter) to context static
2022-12-18 01:27:30,541 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.yarn.webapp.WebApps: Registered webapp guice modules
2022-12-18 01:27:30,542 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.http.HttpServer2: Jetty bound to port 34323
2022-12-18 01:27:30,542 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.Server: jetty-9.4.43.v20210629; built: 2021-06-30T11:07:22.254Z; git: 526006ecfa3af7f1a27ef3a288e2bef7ea9dd7e8; jvm 1.8.0_345-b01
2022-12-18 01:27:30,556 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.session: DefaultSessionIdManager workerName=node0
2022-12-18 01:27:30,556 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.session: No SessionScavenger set, using defaults
2022-12-18 01:27:30,557 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.session: node0 Scavenging every 660000ms
2022-12-18 01:27:30,563 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.handler.ContextHandler: Started o.e.j.s.ServletContextHandler@4b54af3d{static,/static,jar:file:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar!/webapps/static,AVAILABLE}
2022-12-18 01:27:30,967 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.handler.ContextHandler: Started o.e.j.w.WebAppContext@4d09cade{mapreduce,/,file:///data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001/tmp/jetty-0_0_0_0-34323-hadoop-yarn-common-3_3_4_jar-_-any-8456777525715043818/webapp/,AVAILABLE}{jar:file:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar!/webapps/mapreduce}
2022-12-18 01:27:30,972 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.AbstractConnector: Started ServerConnector@34e20e6b{HTTP/1.1, (http/1.1)}{0.0.0.0:34323}
2022-12-18 01:27:30,972 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.Server: Started @2075ms
2022-12-18 01:27:30,972 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.yarn.webapp.WebApps: Web app mapreduce started at 34323
2022-12-18 01:27:30,974 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.speculate.DefaultSpeculator: JOB_CREATE job_1671326373437_0001
2022-12-18 01:27:30,975 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.ipc.CallQueueManager: Using callQueue: class java.util.concurrent.LinkedBlockingQueue, queueCapacity: 3000, scheduler: class org.apache.hadoop.ipc.DefaultRpcScheduler, ipcBackoff: false.
2022-12-18 01:27:30,975 INFO [Socket Reader #1 for port 0] org.apache.hadoop.ipc.Server: Starting Socket Reader #1 for port 0
2022-12-18 01:27:30,978 INFO [IPC Server Responder] org.apache.hadoop.ipc.Server: IPC Server Responder: starting
2022-12-18 01:27:30,978 INFO [IPC Server listener on 0] org.apache.hadoop.ipc.Server: IPC Server listener on 0: starting
2022-12-18 01:27:30,991 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerRequestor: nodeBlacklistingEnabled:true
2022-12-18 01:27:30,991 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerRequestor: maxTaskFailuresPerNode is 3
2022-12-18 01:27:30,991 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerRequestor: blacklistDisablePercent is 33
2022-12-18 01:27:30,993 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: 0% of the mappers will be scheduled using OPPORTUNISTIC containers
2022-12-18 01:27:31,008 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.yarn.client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at resourcemanager/10.0.1.3:8030
2022-12-18 01:27:31,068 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator: maxContainerCapability: <memory:8192, vCores:4>
2022-12-18 01:27:31,068 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator: queue: default
2022-12-18 01:27:31,070 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Upper limit on the thread pool size is 500
2022-12-18 01:27:31,070 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: The thread pool initial size is 10
2022-12-18 01:27:31,081 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: job_1671326373437_0001Job Transitioned from INITED to SETUP
2022-12-18 01:27:31,082 INFO [CommitterEvent Processor #0] org.apache.hadoop.mapreduce.v2.app.commit.CommitterEventHandler: Processing the event EventType: JOB_SETUP
2022-12-18 01:27:31,091 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: job_1671326373437_0001Job Transitioned from SETUP to RUNNING
2022-12-18 01:27:31,104 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: Resource capability of task type MAP is set to <memory:1024, vCores:1>
2022-12-18 01:27:31,105 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: task_1671326373437_0001_m_000000 Task Transitioned from NEW to SCHEDULED
2022-12-18 01:27:31,106 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: task_1671326373437_0001_m_000001 Task Transitioned from NEW to SCHEDULED
2022-12-18 01:27:31,106 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000000_0 TaskAttempt Transitioned from NEW to UNASSIGNED
2022-12-18 01:27:31,107 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000001_0 TaskAttempt Transitioned from NEW to UNASSIGNED
2022-12-18 01:27:31,107 INFO [Thread-60] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: mapResourceRequest:<memory:1024, vCores:1>
2022-12-18 01:27:31,131 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Event Writer setup for JobId: job_1671326373437_0001, File: hdfs://namenode:8020/tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job_1671326373437_0001_1.jhist
2022-12-18 01:27:32,070 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Before Scheduling: PendingReds:0 ScheduledMaps:2 ScheduledReds:0 AssignedMaps:0 AssignedReds:0 CompletedMaps:0 CompletedReds:0 ContAlloc:0 ContRel:0 HostLocal:0 RackLocal:0
2022-12-18 01:27:32,103 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerRequestor: getResources() for application_1671326373437_0001: ask=1 release= 0 newContainers=0 finishedContainers=0 resourcelimit=<memory:6144, vCores:7> knownNMs=1
2022-12-18 01:27:33,114 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Got allocated containers 1
2022-12-18 01:27:33,116 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Assigned container container_1671326373437_0001_01_000002 to attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:33,117 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: After Scheduling: PendingReds:0 ScheduledMaps:1 ScheduledReds:0 AssignedMaps:1 AssignedReds:0 CompletedMaps:0 CompletedReds:0 ContAlloc:1 ContRel:0 HostLocal:0 RackLocal:0
2022-12-18 01:27:33,158 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: The job-jar file on the remote FS is hdfs://namenode:8020/tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job.jar
2022-12-18 01:27:33,161 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: The job-conf file on the remote FS is /tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job.xml
2022-12-18 01:27:33,164 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: Adding #0 tokens and #1 secret keys for NM use for launching container
2022-12-18 01:27:33,164 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: Size of containertokens_dob is 1
2022-12-18 01:27:33,164 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: Putting shuffle token in serviceData
2022-12-18 01:27:33,188 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapred.JobConf: Task java-opts do not specify heap size. Setting task attempt jvm max heap size to -Xmx820m
2022-12-18 01:27:33,190 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000000_0 TaskAttempt Transitioned from UNASSIGNED to ASSIGNED
2022-12-18 01:27:33,193 INFO [ContainerLauncher #0] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Processing the event EventType: CONTAINER_REMOTE_LAUNCH for container container_1671326373437_0001_01_000002 taskAttempt attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:33,195 INFO [ContainerLauncher #0] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Launching attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:33,243 INFO [ContainerLauncher #0] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Shuffle port returned by ContainerManager for attempt_1671326373437_0001_m_000000_0 : 13562
2022-12-18 01:27:33,244 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: TaskAttempt: [attempt_1671326373437_0001_m_000000_0] using containerId: [container_1671326373437_0001_01_000002 on NM: [hadoopnode:36113]
2022-12-18 01:27:33,246 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000000_0 TaskAttempt Transitioned from ASSIGNED to RUNNING
2022-12-18 01:27:33,246 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.speculate.DefaultSpeculator: ATTEMPT_START task_1671326373437_0001_m_000000
2022-12-18 01:27:33,246 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: task_1671326373437_0001_m_000000 Task Transitioned from SCHEDULED to RUNNING
2022-12-18 01:27:33,914 INFO [Socket Reader #1 for port 0] SecurityLogger.org.apache.hadoop.ipc.Server: Auth successful for job_1671326373437_0001 (auth:SIMPLE) from 10.0.1.4:59964
2022-12-18 01:27:33,928 INFO [IPC Server handler 0 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: JVM with ID : jvm_1671326373437_0001_m_000002 asked for a task
2022-12-18 01:27:33,928 INFO [IPC Server handler 0 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: JVM with ID: jvm_1671326373437_0001_m_000002 given task: attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:34,120 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerRequestor: getResources() for application_1671326373437_0001: ask=1 release= 0 newContainers=1 finishedContainers=0 resourcelimit=<memory:4096, vCores:5> knownNMs=1
2022-12-18 01:27:34,120 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Got allocated containers 1
2022-12-18 01:27:34,121 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Assigned container container_1671326373437_0001_01_000003 to attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:34,121 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: After Scheduling: PendingReds:0 ScheduledMaps:0 ScheduledReds:0 AssignedMaps:2 AssignedReds:0 CompletedMaps:0 CompletedReds:0 ContAlloc:2 ContRel:0 HostLocal:0 RackLocal:0
2022-12-18 01:27:34,122 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapred.JobConf: Task java-opts do not specify heap size. Setting task attempt jvm max heap size to -Xmx820m
2022-12-18 01:27:34,122 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000001_0 TaskAttempt Transitioned from UNASSIGNED to ASSIGNED
2022-12-18 01:27:34,122 INFO [ContainerLauncher #1] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Processing the event EventType: CONTAINER_REMOTE_LAUNCH for container container_1671326373437_0001_01_000003 taskAttempt attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:34,122 INFO [ContainerLauncher #1] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Launching attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:34,129 INFO [ContainerLauncher #1] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Shuffle port returned by ContainerManager for attempt_1671326373437_0001_m_000001_0 : 13562
2022-12-18 01:27:34,130 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: TaskAttempt: [attempt_1671326373437_0001_m_000001_0] using containerId: [container_1671326373437_0001_01_000003 on NM: [hadoopnode:36113]
2022-12-18 01:27:34,130 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000001_0 TaskAttempt Transitioned from ASSIGNED to RUNNING
2022-12-18 01:27:34,130 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.speculate.DefaultSpeculator: ATTEMPT_START task_1671326373437_0001_m_000001
2022-12-18 01:27:34,130 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: task_1671326373437_0001_m_000001 Task Transitioned from SCHEDULED to RUNNING
2022-12-18 01:27:34,772 INFO [IPC Server handler 0 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Progress of TaskAttempt attempt_1671326373437_0001_m_000000_0 is : 0.0
2022-12-18 01:27:34,833 INFO [IPC Server handler 2 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Commit-pending state update from attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:34,833 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000000_0 TaskAttempt Transitioned from RUNNING to COMMIT_PENDING
2022-12-18 01:27:34,833 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: attempt_1671326373437_0001_m_000000_0 given a go for committing the task output.
2022-12-18 01:27:34,834 INFO [IPC Server handler 1 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Commit go/no-go request from attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:34,834 INFO [IPC Server handler 1 on default port 45261] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: Result of canCommit for attempt_1671326373437_0001_m_000000_0:true
2022-12-18 01:27:34,859 INFO [IPC Server handler 3 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Progress of TaskAttempt attempt_1671326373437_0001_m_000000_0 is : 1.0
2022-12-18 01:27:34,859 INFO [Socket Reader #1 for port 0] SecurityLogger.org.apache.hadoop.ipc.Server: Auth successful for job_1671326373437_0001 (auth:SIMPLE) from 10.0.1.4:59974
2022-12-18 01:27:34,863 INFO [IPC Server handler 4 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Done acknowledgment from attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:34,865 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000000_0 TaskAttempt Transitioned from COMMIT_PENDING to SUCCESS_FINISHING_CONTAINER
2022-12-18 01:27:34,867 INFO [IPC Server handler 5 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: JVM with ID : jvm_1671326373437_0001_m_000003 asked for a task
2022-12-18 01:27:34,867 INFO [IPC Server handler 5 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: JVM with ID: jvm_1671326373437_0001_m_000003 given task: attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:34,870 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: Task succeeded with attempt attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:34,871 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: task_1671326373437_0001_m_000000 Task Transitioned from RUNNING to SUCCEEDED
2022-12-18 01:27:34,872 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Num completed Tasks: 1
2022-12-18 01:27:35,121 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Before Scheduling: PendingReds:0 ScheduledMaps:0 ScheduledReds:0 AssignedMaps:2 AssignedReds:0 CompletedMaps:1 CompletedReds:0 ContAlloc:2 ContRel:0 HostLocal:0 RackLocal:0
2022-12-18 01:27:35,124 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerRequestor: getResources() for application_1671326373437_0001: ask=1 release= 0 newContainers=1 finishedContainers=0 resourcelimit=<memory:3072, vCores:4> knownNMs=1
2022-12-18 01:27:35,124 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Got allocated containers 1
2022-12-18 01:27:35,124 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Cannot assign container Container: [ContainerId: container_1671326373437_0001_01_000004, AllocationRequestId: -1, Version: 0, NodeId: hadoopnode:36113, NodeHttpAddress: hadoopnode:8042, Resource: <memory:1024, vCores:1>, Priority: 20, Token: Token { kind: ContainerToken, service: 10.0.1.4:36113 }, ExecutionType: GUARANTEED, ] for a map as either  container memory less than required <memory:1024, vCores:1> or no pending map tasks - maps.isEmpty=true
2022-12-18 01:27:35,125 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: After Scheduling: PendingReds:0 ScheduledMaps:0 ScheduledReds:0 AssignedMaps:2 AssignedReds:0 CompletedMaps:1 CompletedReds:0 ContAlloc:3 ContRel:1 HostLocal:0 RackLocal:0
2022-12-18 01:27:35,634 INFO [IPC Server handler 0 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Progress of TaskAttempt attempt_1671326373437_0001_m_000001_0 is : 0.0
2022-12-18 01:27:35,688 INFO [IPC Server handler 2 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Commit-pending state update from attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:35,688 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000001_0 TaskAttempt Transitioned from RUNNING to COMMIT_PENDING
2022-12-18 01:27:35,688 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: attempt_1671326373437_0001_m_000001_0 given a go for committing the task output.
2022-12-18 01:27:35,689 INFO [IPC Server handler 1 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Commit go/no-go request from attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:35,689 INFO [IPC Server handler 1 on default port 45261] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: Result of canCommit for attempt_1671326373437_0001_m_000001_0:true
2022-12-18 01:27:35,700 INFO [IPC Server handler 3 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Progress of TaskAttempt attempt_1671326373437_0001_m_000001_0 is : 1.0
2022-12-18 01:27:35,701 INFO [IPC Server handler 4 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Done acknowledgment from attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:35,702 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000001_0 TaskAttempt Transitioned from COMMIT_PENDING to SUCCESS_FINISHING_CONTAINER
2022-12-18 01:27:35,702 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: Task succeeded with attempt attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:35,702 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: task_1671326373437_0001_m_000001 Task Transitioned from RUNNING to SUCCEEDED
2022-12-18 01:27:35,702 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Num completed Tasks: 2
2022-12-18 01:27:35,703 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: job_1671326373437_0001Job Transitioned from RUNNING to COMMITTING
2022-12-18 01:27:35,703 INFO [CommitterEvent Processor #1] org.apache.hadoop.mapreduce.v2.app.commit.CommitterEventHandler: Processing the event EventType: JOB_COMMIT
2022-12-18 01:27:35,727 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Calling handler for JobFinishedEvent 
2022-12-18 01:27:35,727 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: job_1671326373437_0001Job Transitioned from COMMITTING to SUCCEEDED
2022-12-18 01:27:35,728 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Job finished cleanly, recording last MRAppMaster retry
2022-12-18 01:27:35,728 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Notify RMCommunicator isAMLastRetry: true
2022-12-18 01:27:35,728 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator: RMCommunicator notified that shouldUnregistered is: true
2022-12-18 01:27:35,728 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Notify JHEH isAMLastRetry: true
2022-12-18 01:27:35,728 INFO [Thread-75] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: JobHistoryEventHandler notified that forceJobCompletion is true
2022-12-18 01:27:35,728 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Calling stop for all the services
2022-12-18 01:27:35,729 INFO [Thread-75] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Stopping JobHistoryEventHandler. Size of the outstanding queue size is 0
2022-12-18 01:27:35,750 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Copying hdfs://namenode:8020/tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job_1671326373437_0001_1.jhist to hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001-1671326847669-sandbox-TeraGen-1671326855725-2-0-SUCCEEDED-default-1671326851073.jhist_tmp
2022-12-18 01:27:35,771 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Copied from: hdfs://namenode:8020/tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job_1671326373437_0001_1.jhist to done location: hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001-1671326847669-sandbox-TeraGen-1671326855725-2-0-SUCCEEDED-default-1671326851073.jhist_tmp
2022-12-18 01:27:35,772 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Set historyUrl to http://jobhistoryserver:19888/jobhistory/job/job_1671326373437_0001
2022-12-18 01:27:35,773 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Copying hdfs://namenode:8020/tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job_1671326373437_0001_1_conf.xml to hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001_conf.xml_tmp
2022-12-18 01:27:35,790 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Copied from: hdfs://namenode:8020/tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job_1671326373437_0001_1_conf.xml to done location: hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001_conf.xml_tmp
2022-12-18 01:27:35,795 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Moved tmp to done: hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001.summary_tmp to hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001.summary
2022-12-18 01:27:35,797 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Moved tmp to done: hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001_conf.xml_tmp to hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001_conf.xml
2022-12-18 01:27:35,798 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Moved tmp to done: hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001-1671326847669-sandbox-TeraGen-1671326855725-2-0-SUCCEEDED-default-1671326851073.jhist_tmp to hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001-1671326847669-sandbox-TeraGen-1671326855725-2-0-SUCCEEDED-default-1671326851073.jhist
2022-12-18 01:27:35,799 INFO [Thread-75] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Stopped JobHistoryEventHandler. super.stop()
2022-12-18 01:27:35,799 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: KILLING attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:35,821 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: KILLING attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:35,821 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000001_0 TaskAttempt Transitioned from SUCCESS_FINISHING_CONTAINER to SUCCEEDED
2022-12-18 01:27:35,827 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000000_0 TaskAttempt Transitioned from SUCCESS_FINISHING_CONTAINER to SUCCEEDED
2022-12-18 01:27:35,828 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator: Setting job diagnostics to 
2022-12-18 01:27:35,828 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator: History url is http://jobhistoryserver:19888/jobhistory/job/job_1671326373437_0001
2022-12-18 01:27:35,840 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator: Waiting for application to be successfully unregistered.
2022-12-18 01:27:36,841 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Final Stats: PendingReds:0 ScheduledMaps:0 ScheduledReds:0 AssignedMaps:2 AssignedReds:0 CompletedMaps:1 CompletedReds:0 ContAlloc:3 ContRel:1 HostLocal:0 RackLocal:0
2022-12-18 01:27:36,842 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Deleting staging directory hdfs://namenode:8020 /tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001
2022-12-18 01:27:36,849 INFO [Thread-75] org.apache.hadoop.ipc.Server: Stopping server on 45261
2022-12-18 01:27:36,850 INFO [IPC Server listener on 0] org.apache.hadoop.ipc.Server: Stopping IPC Server listener on 0
2022-12-18 01:27:36,850 INFO [IPC Server Responder] org.apache.hadoop.ipc.Server: Stopping IPC Server Responder
2022-12-18 01:27:36,850 INFO [TaskHeartbeatHandler PingChecker] org.apache.hadoop.mapreduce.v2.app.TaskHeartbeatHandler: TaskHeartbeatHandler thread interrupted
2022-12-18 01:27:36,851 INFO [Ping Checker for TaskAttemptFinishingMonitor] org.apache.hadoop.yarn.util.AbstractLivelinessMonitor: TaskAttemptFinishingMonitor thread interrupted
2022-12-18 01:27:41,851 INFO [Thread-75] org.apache.hadoop.ipc.Server: Stopping server on 39881
2022-12-18 01:27:41,851 INFO [IPC Server listener on 0] org.apache.hadoop.ipc.Server: Stopping IPC Server listener on 0
2022-12-18 01:27:41,851 INFO [IPC Server Responder] org.apache.hadoop.ipc.Server: Stopping IPC Server Responder
2022-12-18 01:27:41,853 INFO [Thread-75] org.eclipse.jetty.server.handler.ContextHandler: Stopped o.e.j.w.WebAppContext@4d09cade{mapreduce,/,null,STOPPED}{jar:file:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar!/webapps/mapreduce}
2022-12-18 01:27:41,857 INFO [Thread-75] org.eclipse.jetty.server.AbstractConnector: Stopped ServerConnector@34e20e6b{HTTP/1.1, (http/1.1)}{0.0.0.0:0}
2022-12-18 01:27:41,857 INFO [Thread-75] org.eclipse.jetty.server.session: node0 Stopped scavenging
2022-12-18 01:27:41,857 INFO [Thread-75] org.eclipse.jetty.server.handler.ContextHandler: Stopped o.e.j.s.ServletContextHandler@4b54af3d{static,/static,jar:file:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar!/webapps/static,STOPPED}

End of LogType:syslog
***********************************************************************

"""

OUTPUT_FIXTURE = {
    "hadoopnode": {
        "container_1671326373437_0001_01_000001": {
            "directory.info": b"""ls -l:
total 36
-rw-r--r-- 1 yarn yarn  105 Dec 18 01:27 container_tokens
-rwx------ 1 yarn yarn  627 Dec 18 01:27 default_container_executor_session.sh
-rwx------ 1 yarn yarn  682 Dec 18 01:27 default_container_executor.sh
lrwxrwxrwx 1 yarn yarn   97 Dec 18 01:27 job.jar -> /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/11/job.jar
drwxr-xr-x 2 yarn yarn 4096 Dec 18 01:27 jobSubmitDir
lrwxrwxrwx 1 yarn yarn   97 Dec 18 01:27 job.xml -> /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/13/job.xml
-rwx------ 1 yarn yarn 4954 Dec 18 01:27 launch_container.sh
drwx--x--- 2 yarn yarn 4096 Dec 18 01:27 tmp
find -L . -maxdepth 5 -ls:
 63318123      4 drwx--x---   4 yarn     yarn         4096 Dec 18 01:27 .
 63318125      4 drwx--x---   2 yarn     yarn         4096 Dec 18 01:27 ./tmp
 63318132      4 -rwx------   1 yarn     yarn          682 Dec 18 01:27 ./default_container_executor.sh
 63318130      4 -rwx------   1 yarn     yarn          627 Dec 18 01:27 ./default_container_executor_session.sh
 63318129      4 -rw-r--r--   1 yarn     yarn           48 Dec 18 01:27 ./.launch_container.sh.crc
 63317898      4 drwx------   2 yarn     yarn         4096 Dec 18 01:27 ./job.jar
 63317919    276 -r-x------   1 yarn     yarn       280992 Dec 18 01:27 ./job.jar/job.jar
 63318131      4 -rw-r--r--   1 yarn     yarn           16 Dec 18 01:27 ./.default_container_executor_session.sh.crc
 63318115    232 -r-x------   1 yarn     yarn       235968 Dec 18 01:27 ./job.xml
 63318126      4 -rw-r--r--   1 yarn     yarn          105 Dec 18 01:27 ./container_tokens
 63318138      4 drwxr-xr-x   2 yarn     yarn         4096 Dec 18 01:27 ./jobSubmitDir
 63318112      4 -r-x------   1 yarn     yarn          174 Dec 18 01:27 ./jobSubmitDir/job.split
 63318105      4 -r-x------   1 yarn     yarn           16 Dec 18 01:27 ./jobSubmitDir/job.splitmetainfo
 63318128      8 -rwx------   1 yarn     yarn         4954 Dec 18 01:27 ./launch_container.sh
 63318127      4 -rw-r--r--   1 yarn     yarn           12 Dec 18 01:27 ./.container_tokens.crc
 63318133      4 -rw-r--r--   1 yarn     yarn           16 Dec 18 01:27 ./.default_container_executor.sh.crc
broken symlinks(find -L . -maxdepth 5 -type l -ls):
""",
            "launch_container.sh": b"""#!/bin/bash

set -o pipefail -e
export PRELAUNCH_OUT="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/prelaunch.out"
exec >"${PRELAUNCH_OUT}"
export PRELAUNCH_ERR="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/prelaunch.err"
exec 2>"${PRELAUNCH_ERR}"
echo "Setting up env variables"
export JAVA_HOME=${JAVA_HOME:-"/opt/java/openjdk"}
export HADOOP_COMMON_HOME=${HADOOP_COMMON_HOME:-"/hadoop"}
export HADOOP_HDFS_HOME=${HADOOP_HDFS_HOME:-"/hadoop"}
export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/hadoop/etc/hadoop"}
export HADOOP_YARN_HOME=${HADOOP_YARN_HOME:-"/hadoop"}
export HADOOP_HOME=${HADOOP_HOME:-"/hadoop"}
export PATH=${PATH:-"/hadoop/bin:/hadoop/sbin:/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"}
export LANG=${LANG:-"en_US.UTF-8"}
export HADOOP_MAPRED_HOME=${HADOOP_MAPRED_HOME:-"/hadoop"}
export HADOOP_TOKEN_FILE_LOCATION="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001/container_tokens"
export CONTAINER_ID="container_1671326373437_0001_01_000001"
export NM_PORT="36113"
export NM_HOST="hadoopnode"
export NM_HTTP_PORT="8042"
export LOCAL_DIRS="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001"
export LOCAL_USER_DIRS="/data/nm-local-dir/usercache/sandbox/"
export LOG_DIRS="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001"
export USER="sandbox"
export LOGNAME="sandbox"
export HOME="/home/"
export PWD="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001"
export LOCALIZATION_COUNTERS="519026,0,4,0,296"
export JVM_PID="$$"
export NM_AUX_SERVICE_mapreduce_shuffle="AAA0+gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
export APPLICATION_WEB_PROXY_BASE="/proxy/application_1671326373437_0001"
export SHELL="/bin/bash"
export CLASSPATH="$PWD:$HADOOP_CONF_DIR:$HADOOP_COMMON_HOME/share/hadoop/common/*:$HADOOP_COMMON_HOME/share/hadoop/common/lib/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/lib/*:$HADOOP_YARN_HOME/share/hadoop/yarn/*:$HADOOP_YARN_HOME/share/hadoop/yarn/lib/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*:job.jar/*:job.jar/classes/:job.jar/lib/*:$PWD/*"
export APP_SUBMIT_TIME_ENV="1671326847669"
export LD_LIBRARY_PATH="$PWD:$HADOOP_COMMON_HOME/lib/native"
export MALLOC_ARENA_MAX="4"
echo "Setting up job resources"
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/11/job.jar" "job.jar"
mkdir -p jobSubmitDir
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/10/job.splitmetainfo" "jobSubmitDir/job.splitmetainfo"
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/13/job.xml" "job.xml"
mkdir -p jobSubmitDir
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/12/job.split" "jobSubmitDir/job.split"
echo "Copying debugging information"
# Creating copy of launch script
cp "launch_container.sh" "/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/launch_container.sh"
chmod 640 "/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/launch_container.sh"
# Determining directory contents
echo "ls -l:" 1>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/directory.info"
ls -l 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/directory.info"
echo "find -L . -maxdepth 5 -ls:" 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/directory.info"
find -L . -maxdepth 5 -ls 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/directory.info"
echo "broken symlinks(find -L . -maxdepth 5 -type l -ls):" 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/directory.info"
find -L . -maxdepth 5 -type l -ls 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/directory.info"
echo "Launching container"
exec /bin/bash -c "$JAVA_HOME/bin/java -Djava.io.tmpdir=$PWD/tmp -Dlog4j.configuration=container-log4j.properties -Dyarn.app.container.log.dir=/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001 -Dyarn.app.container.log.filesize=0 -Dhadoop.root.logger=INFO,CLA -Dhadoop.root.logfile=syslog  -Xmx1024m org.apache.hadoop.mapreduce.v2.app.MRAppMaster 1>/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/stdout 2>/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000001/stderr "
""",
            "prelaunch.err": b"""""",
            "prelaunch.out": b"""Setting up env variables
Setting up job resources
Copying debugging information
Launching container
""",
            "stderr": b"""Dec 18, 2022 1:27:30 AM com.sun.jersey.guice.spi.container.GuiceComponentProviderFactory register
INFO: Registering org.apache.hadoop.mapreduce.v2.app.webapp.JAXBContextResolver as a provider class
Dec 18, 2022 1:27:30 AM com.sun.jersey.guice.spi.container.GuiceComponentProviderFactory register
INFO: Registering org.apache.hadoop.yarn.webapp.GenericExceptionHandler as a provider class
Dec 18, 2022 1:27:30 AM com.sun.jersey.guice.spi.container.GuiceComponentProviderFactory register
INFO: Registering org.apache.hadoop.mapreduce.v2.app.webapp.AMWebServices as a root resource class
Dec 18, 2022 1:27:30 AM com.sun.jersey.server.impl.application.WebApplicationImpl _initiate
INFO: Initiating Jersey application, version 'Jersey: 1.19 02/11/2015 03:25 AM'
Dec 18, 2022 1:27:30 AM com.sun.jersey.guice.spi.container.GuiceComponentProviderFactory getComponentProvider
INFO: Binding org.apache.hadoop.mapreduce.v2.app.webapp.JAXBContextResolver to GuiceManagedComponentProvider with the scope "Singleton"
Dec 18, 2022 1:27:30 AM com.sun.jersey.guice.spi.container.GuiceComponentProviderFactory getComponentProvider
INFO: Binding org.apache.hadoop.yarn.webapp.GenericExceptionHandler to GuiceManagedComponentProvider with the scope "Singleton"
Dec 18, 2022 1:27:30 AM com.sun.jersey.guice.spi.container.GuiceComponentProviderFactory getComponentProvider
INFO: Binding org.apache.hadoop.mapreduce.v2.app.webapp.AMWebServices to GuiceManagedComponentProvider with the scope "PerRequest"
log4j:WARN No appenders could be found for logger (org.apache.hadoop.mapreduce.v2.app.MRAppMaster).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
""",
            "stdout": b"""""",
            "syslog": b"""2022-12-18 01:27:29,315 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Created MRAppMaster for application appattempt_1671326373437_0001_000001
2022-12-18 01:27:29,366 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: 
/************************************************************
[system properties]
os.name: Linux
os.version: 6.0.0-6-amd64
java.home: /opt/java/openjdk/jre
java.runtime.version: 1.8.0_345-b01
java.vendor: Temurin
java.version: 1.8.0_345
java.vm.name: OpenJDK 64-Bit Server VM
java.class.path: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001:/hadoop/etc/hadoop:/hadoop/share/hadoop/common/hadoop-nfs-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-kms-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-registry-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-common-3.3.4-tests.jar:/hadoop/share/hadoop/common/hadoop-common-3.3.4.jar:/hadoop/share/hadoop/common/lib/kerby-pkix-1.0.1.jar:/hadoop/share/hadoop/common/lib/nimbus-jose-jwt-9.8.1.jar:/hadoop/share/hadoop/common/lib/jetty-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/asm-5.0.4.jar:/hadoop/share/hadoop/common/lib/paranamer-2.3.jar:/hadoop/share/hadoop/common/lib/commons-configuration2-2.1.1.jar:/hadoop/share/hadoop/common/lib/kerb-identity-1.0.1.jar:/hadoop/share/hadoop/common/lib/re2j-1.1.jar:/hadoop/share/hadoop/common/lib/jackson-xc-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-beanutils-1.9.4.jar:/hadoop/share/hadoop/common/lib/jsch-0.1.55.jar:/hadoop/share/hadoop/common/lib/commons-math3-3.1.1.jar:/hadoop/share/hadoop/common/lib/jackson-mapper-asl-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-security-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-codec-1.15.jar:/hadoop/share/hadoop/common/lib/gson-2.8.9.jar:/hadoop/share/hadoop/common/lib/j2objc-annotations-1.1.jar:/hadoop/share/hadoop/common/lib/jackson-core-asl-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-webapp-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/animal-sniffer-annotations-1.17.jar:/hadoop/share/hadoop/common/lib/jackson-jaxrs-1.9.13.jar:/hadoop/share/hadoop/common/lib/kerby-util-1.0.1.jar:/hadoop/share/hadoop/common/lib/zookeeper-3.5.6.jar:/hadoop/share/hadoop/common/lib/accessors-smart-2.4.7.jar:/hadoop/share/hadoop/common/lib/reload4j-1.2.22.jar:/hadoop/share/hadoop/common/lib/jcip-annotations-1.0-1.jar:/hadoop/share/hadoop/common/lib/jersey-servlet-1.19.jar:/hadoop/share/hadoop/common/lib/metrics-core-3.2.4.jar:/hadoop/share/hadoop/common/lib/jersey-json-1.19.jar:/hadoop/share/hadoop/common/lib/jsp-api-2.1.jar:/hadoop/share/hadoop/common/lib/curator-client-4.2.0.jar:/hadoop/share/hadoop/common/lib/curator-recipes-4.2.0.jar:/hadoop/share/hadoop/common/lib/commons-text-1.4.jar:/hadoop/share/hadoop/common/lib/jersey-server-1.19.jar:/hadoop/share/hadoop/common/lib/kerb-simplekdc-1.0.1.jar:/hadoop/share/hadoop/common/lib/jersey-core-1.19.jar:/hadoop/share/hadoop/common/lib/avro-1.7.7.jar:/hadoop/share/hadoop/common/lib/commons-io-2.8.0.jar:/hadoop/share/hadoop/common/lib/kerb-core-1.0.1.jar:/hadoop/share/hadoop/common/lib/slf4j-api-1.7.36.jar:/hadoop/share/hadoop/common/lib/kerb-server-1.0.1.jar:/hadoop/share/hadoop/common/lib/commons-collections-3.2.2.jar:/hadoop/share/hadoop/common/lib/jackson-core-2.12.7.jar:/hadoop/share/hadoop/common/lib/commons-daemon-1.0.13.jar:/hadoop/share/hadoop/common/lib/snappy-java-1.1.8.2.jar:/hadoop/share/hadoop/common/lib/jettison-1.1.jar:/hadoop/share/hadoop/common/lib/kerb-common-1.0.1.jar:/hadoop/share/hadoop/common/lib/jetty-http-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/failureaccess-1.0.jar:/hadoop/share/hadoop/common/lib/jul-to-slf4j-1.7.36.jar:/hadoop/share/hadoop/common/lib/jaxb-api-2.2.11.jar:/hadoop/share/hadoop/common/lib/jsr311-api-1.1.1.jar:/hadoop/share/hadoop/common/lib/jaxb-impl-2.2.3-1.jar:/hadoop/share/hadoop/common/lib/javax.servlet-api-3.1.0.jar:/hadoop/share/hadoop/common/lib/zookeeper-jute-3.5.6.jar:/hadoop/share/hadoop/common/lib/jetty-util-ajax-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-compress-1.21.jar:/hadoop/share/hadoop/common/lib/commons-net-3.6.jar:/hadoop/share/hadoop/common/lib/commons-cli-1.2.jar:/hadoop/share/hadoop/common/lib/checker-qual-2.5.2.jar:/hadoop/share/hadoop/common/lib/jetty-io-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/netty-3.10.6.Final.jar:/hadoop/share/hadoop/common/lib/kerb-crypto-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerby-asn1-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerby-xdr-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerb-util-1.0.1.jar:/hadoop/share/hadoop/common/lib/commons-logging-1.1.3.jar:/hadoop/share/hadoop/common/lib/commons-lang3-3.12.0.jar:/hadoop/share/hadoop/common/lib/token-provider-1.0.1.jar:/hadoop/share/hadoop/common/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/hadoop/share/hadoop/common/lib/jakarta.activation-api-1.2.1.jar:/hadoop/share/hadoop/common/lib/httpclient-4.5.13.jar:/hadoop/share/hadoop/common/lib/hadoop-shaded-guava-1.1.1.jar:/hadoop/share/hadoop/common/lib/hadoop-annotations-3.3.4.jar:/hadoop/share/hadoop/common/lib/hadoop-auth-3.3.4.jar:/hadoop/share/hadoop/common/lib/jackson-databind-2.12.7.jar:/hadoop/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar:/hadoop/share/hadoop/common/lib/curator-framework-4.2.0.jar:/hadoop/share/hadoop/common/lib/woodstox-core-5.3.0.jar:/hadoop/share/hadoop/common/lib/audience-annotations-0.5.0.jar:/hadoop/share/hadoop/common/lib/kerb-client-1.0.1.jar:/hadoop/share/hadoop/common/lib/json-smart-2.4.7.jar:/hadoop/share/hadoop/common/lib/dnsjava-2.1.7.jar:/hadoop/share/hadoop/common/lib/jsr305-3.0.2.jar:/hadoop/share/hadoop/common/lib/kerb-admin-1.0.1.jar:/hadoop/share/hadoop/common/lib/httpcore-4.4.13.jar:/hadoop/share/hadoop/common/lib/protobuf-java-2.5.0.jar:/hadoop/share/hadoop/common/lib/kerby-config-1.0.1.jar:/hadoop/share/hadoop/common/lib/jetty-util-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/jackson-annotations-2.12.7.jar:/hadoop/share/hadoop/common/lib/jetty-xml-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/hadoop-shaded-protobuf_3_7-1.1.1.jar:/hadoop/share/hadoop/common/lib/stax2-api-4.2.1.jar:/hadoop/share/hadoop/common/lib/guava-27.0-jre.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-native-client-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-rbf-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-rbf-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-native-client-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-httpfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-client-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-client-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-nfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/kerby-pkix-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/nimbus-jose-jwt-9.8.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/asm-5.0.4.jar:/hadoop/share/hadoop/hdfs/lib/paranamer-2.3.jar:/hadoop/share/hadoop/hdfs/lib/commons-configuration2-2.1.1.jar:/hadoop/share/hadoop/hdfs/lib/kerb-identity-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/re2j-1.1.jar:/hadoop/share/hadoop/hdfs/lib/jackson-xc-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/jetty-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-beanutils-1.9.4.jar:/hadoop/share/hadoop/hdfs/lib/leveldbjni-all-1.8.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-dns-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-rxtx-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jsch-0.1.55.jar:/hadoop/share/hadoop/hdfs/lib/commons-math3-3.1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-http2-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-udt-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jackson-mapper-asl-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/okhttp-4.9.3.jar:/hadoop/share/hadoop/hdfs/lib/jetty-security-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/commons-codec-1.15.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-mqtt-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-native-macos-4.1.77.Final-osx-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/gson-2.8.9.jar:/hadoop/share/hadoop/hdfs/lib/j2objc-annotations-1.1.jar:/hadoop/share/hadoop/hdfs/lib/jackson-core-asl-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/jetty-webapp-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/animal-sniffer-annotations-1.17.jar:/hadoop/share/hadoop/hdfs/lib/okio-2.8.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-handler-proxy-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jackson-jaxrs-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/kerby-util-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/zookeeper-3.5.6.jar:/hadoop/share/hadoop/hdfs/lib/accessors-smart-2.4.7.jar:/hadoop/share/hadoop/hdfs/lib/reload4j-1.2.22.jar:/hadoop/share/hadoop/hdfs/lib/jcip-annotations-1.0-1.jar:/hadoop/share/hadoop/hdfs/lib/jersey-servlet-1.19.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-kqueue-4.1.77.Final-osx-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/jersey-json-1.19.jar:/hadoop/share/hadoop/hdfs/lib/curator-client-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/curator-recipes-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/commons-text-1.4.jar:/hadoop/share/hadoop/hdfs/lib/kotlin-stdlib-common-1.4.10.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-unix-common-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-all-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-epoll-4.1.77.Final-linux-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/jersey-server-1.19.jar:/hadoop/share/hadoop/hdfs/lib/netty-common-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-simplekdc-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jersey-core-1.19.jar:/hadoop/share/hadoop/hdfs/lib/avro-1.7.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-io-2.8.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-haproxy-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-core-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-sctp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-server-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/commons-collections-3.2.2.jar:/hadoop/share/hadoop/hdfs/lib/jackson-core-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-http-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-daemon-1.0.13.jar:/hadoop/share/hadoop/hdfs/lib/snappy-java-1.1.8.2.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-classes-epoll-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jettison-1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-smtp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-common-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-http-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/failureaccess-1.0.jar:/hadoop/share/hadoop/hdfs/lib/kotlin-stdlib-1.4.10.jar:/hadoop/share/hadoop/hdfs/lib/jaxb-api-2.2.11.jar:/hadoop/share/hadoop/hdfs/lib/netty-buffer-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-classes-macos-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jsr311-api-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/json-simple-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-stomp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jaxb-impl-2.2.3-1.jar:/hadoop/share/hadoop/hdfs/lib/javax.servlet-api-3.1.0.jar:/hadoop/share/hadoop/hdfs/lib/zookeeper-jute-3.5.6.jar:/hadoop/share/hadoop/hdfs/lib/jetty-util-ajax-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-epoll-4.1.77.Final-linux-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/netty-handler-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-compress-1.21.jar:/hadoop/share/hadoop/hdfs/lib/commons-net-3.6.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-xml-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-cli-1.2.jar:/hadoop/share/hadoop/hdfs/lib/checker-qual-2.5.2.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-kqueue-4.1.77.Final-osx-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-memcache-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jetty-io-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-3.10.6.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-crypto-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerby-asn1-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerby-xdr-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerb-util-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/commons-logging-1.1.3.jar:/hadoop/share/hadoop/hdfs/lib/commons-lang3-3.12.0.jar:/hadoop/share/hadoop/hdfs/lib/token-provider-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/hadoop/share/hadoop/hdfs/lib/jakarta.activation-api-1.2.1.jar:/hadoop/share/hadoop/hdfs/lib/httpclient-4.5.13.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-redis-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-shaded-guava-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-annotations-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-auth-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/jackson-databind-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/curator-framework-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-native-macos-4.1.77.Final-osx-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/woodstox-core-5.3.0.jar:/hadoop/share/hadoop/hdfs/lib/audience-annotations-0.5.0.jar:/hadoop/share/hadoop/hdfs/lib/kerb-client-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/json-smart-2.4.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-socks-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-classes-kqueue-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/dnsjava-2.1.7.jar:/hadoop/share/hadoop/hdfs/lib/jsr305-3.0.2.jar:/hadoop/share/hadoop/hdfs/lib/kerb-admin-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/httpcore-4.4.13.jar:/hadoop/share/hadoop/hdfs/lib/protobuf-java-2.5.0.jar:/hadoop/share/hadoop/hdfs/lib/kerby-config-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-util-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/jackson-annotations-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/jetty-xml-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-shaded-protobuf_3_7-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/stax2-api-4.2.1.jar:/hadoop/share/hadoop/hdfs/lib/guava-27.0-jre.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-registry-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-router-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-client-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-distributedshell-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-services-core-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-nodemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-api-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-resourcemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-mawo-core-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-services-api-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-tests-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-unmanaged-am-launcher-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-sharedcachemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-web-proxy-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-timeline-pluginstorage-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-applicationhistoryservice-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-common-3.3.4.jar:/hadoop/share/hadoop/yarn/lib/javax.websocket-api-1.0.jar:/hadoop/share/hadoop/yarn/lib/websocket-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/json-io-2.5.1.jar:/hadoop/share/hadoop/yarn/lib/jline-3.9.0.jar:/hadoop/share/hadoop/yarn/lib/bcprov-jdk15on-1.60.jar:/hadoop/share/hadoop/yarn/lib/websocket-common-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jetty-jndi-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/websocket-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jackson-module-jaxb-annotations-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/HikariCP-java7-2.4.12.jar:/hadoop/share/hadoop/yarn/lib/jersey-client-1.19.jar:/hadoop/share/hadoop/yarn/lib/metrics-core-3.2.4.jar:/hadoop/share/hadoop/yarn/lib/jetty-client-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/guice-servlet-4.0.jar:/hadoop/share/hadoop/yarn/lib/swagger-annotations-1.5.4.jar:/hadoop/share/hadoop/yarn/lib/bcpkix-jdk15on-1.60.jar:/hadoop/share/hadoop/yarn/lib/websocket-api-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jna-5.2.0.jar:/hadoop/share/hadoop/yarn/lib/jackson-jaxrs-base-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/javax-websocket-client-impl-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/snakeyaml-1.26.jar:/hadoop/share/hadoop/yarn/lib/asm-tree-9.1.jar:/hadoop/share/hadoop/yarn/lib/javax.websocket-client-api-1.0.jar:/hadoop/share/hadoop/yarn/lib/javax-websocket-server-impl-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jackson-jaxrs-json-provider-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/asm-analysis-9.1.jar:/hadoop/share/hadoop/yarn/lib/websocket-client-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/ehcache-3.3.1.jar:/hadoop/share/hadoop/yarn/lib/guice-4.0.jar:/hadoop/share/hadoop/yarn/lib/fst-2.50.jar:/hadoop/share/hadoop/yarn/lib/jetty-plus-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jetty-annotations-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/geronimo-jcache_1.0_spec-1.0-alpha-1.jar:/hadoop/share/hadoop/yarn/lib/mssql-jdbc-6.2.1.jre7.jar:/hadoop/share/hadoop/yarn/lib/objenesis-2.6.jar:/hadoop/share/hadoop/yarn/lib/jersey-guice-1.19.jar:/hadoop/share/hadoop/yarn/lib/jakarta.xml.bind-api-2.3.2.jar:/hadoop/share/hadoop/yarn/lib/aopalliance-1.0.jar:/hadoop/share/hadoop/yarn/lib/javax.inject-1.jar:/hadoop/share/hadoop/yarn/lib/asm-commons-9.1.jar:/hadoop/share/hadoop/yarn/lib/java-util-1.9.0.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-plugins-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-shuffle-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.4-tests.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-nativetask-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-app-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-uploader-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.3.4.jar:/hadoop/share/hadoop/mapreduce/lib/*:job.jar/job.jar:job.jar/classes/:job.jar/lib/*:/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001/job.jar
java.io.tmpdir: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001/tmp
user.dir: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001
user.name: yarn
************************************************************/
2022-12-18 01:27:29,393 INFO [main] org.apache.hadoop.security.SecurityUtil: Updating Configuration
2022-12-18 01:27:29,453 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Executing with tokens: [Kind: YARN_AM_RM_TOKEN, Service: , Ident: (appAttemptId { application_id { id: 1 cluster_timestamp: 1671326373437 } attemptId: 1 } keyId: -928306625)]
2022-12-18 01:27:29,471 INFO [main] org.apache.hadoop.conf.Configuration: resource-types.xml not found
2022-12-18 01:27:29,472 INFO [main] org.apache.hadoop.yarn.util.resource.ResourceUtils: Unable to find 'resource-types.xml'.
2022-12-18 01:27:29,478 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Using mapred newApiCommitter.
2022-12-18 01:27:29,479 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: OutputCommitter set in config null
2022-12-18 01:27:29,497 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: File Output Committer Algorithm version is 2
2022-12-18 01:27:29,497 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2022-12-18 01:27:29,739 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: OutputCommitter is org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter
2022-12-18 01:27:29,796 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.jobhistory.EventType for class org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler
2022-12-18 01:27:29,797 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.job.event.JobEventType for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$JobEventDispatcher
2022-12-18 01:27:29,797 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.job.event.TaskEventType for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$TaskEventDispatcher
2022-12-18 01:27:29,797 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.job.event.TaskAttemptEventType for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$TaskAttemptEventDispatcher
2022-12-18 01:27:29,798 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.commit.CommitterEventType for class org.apache.hadoop.mapreduce.v2.app.commit.CommitterEventHandler
2022-12-18 01:27:29,800 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.speculate.Speculator$EventType for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$SpeculatorEventDispatcher
2022-12-18 01:27:29,800 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.rm.ContainerAllocator$EventType for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$ContainerAllocatorRouter
2022-12-18 01:27:29,801 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncher$EventType for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$ContainerLauncherRouter
2022-12-18 01:27:29,813 INFO [main] org.apache.hadoop.mapreduce.v2.jobhistory.JobHistoryUtils: Default file system [hdfs://namenode:8020]
2022-12-18 01:27:29,820 INFO [main] org.apache.hadoop.mapreduce.v2.jobhistory.JobHistoryUtils: Default file system [hdfs://namenode:8020]
2022-12-18 01:27:29,826 INFO [main] org.apache.hadoop.mapreduce.v2.jobhistory.JobHistoryUtils: Default file system [hdfs://namenode:8020]
2022-12-18 01:27:29,839 INFO [main] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Perms after creating 488, Expected: 504
2022-12-18 01:27:29,839 INFO [main] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Explicitly setting permissions to : 504, rwxrwx---
2022-12-18 01:27:29,842 INFO [main] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Emitting job history data to the timeline server is not enabled
2022-12-18 01:27:29,863 INFO [main] org.apache.hadoop.yarn.event.AsyncDispatcher: Registering class org.apache.hadoop.mapreduce.v2.app.job.event.JobFinishEvent$Type for class org.apache.hadoop.mapreduce.v2.app.MRAppMaster$JobFinishEventHandler
2022-12-18 01:27:29,946 INFO [main] org.apache.hadoop.metrics2.impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2022-12-18 01:27:29,977 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 second(s).
2022-12-18 01:27:29,977 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MRAppMaster metrics system started
2022-12-18 01:27:29,981 INFO [main] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Adding job token for job_1671326373437_0001 to jobTokenSecretManager
2022-12-18 01:27:30,079 INFO [main] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Not uberizing job_1671326373437_0001 because: not enabled;
2022-12-18 01:27:30,094 INFO [main] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Input size for job job_1671326373437_0001 = 0. Number of splits = 2
2022-12-18 01:27:30,094 INFO [main] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Number of reduces for job job_1671326373437_0001 = 0
2022-12-18 01:27:30,094 INFO [main] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: job_1671326373437_0001Job Transitioned from NEW to INITED
2022-12-18 01:27:30,095 INFO [main] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: MRAppMaster launching normal, non-uberized, multi-container job job_1671326373437_0001.
2022-12-18 01:27:30,122 INFO [main] org.apache.hadoop.ipc.CallQueueManager: Using callQueue: class java.util.concurrent.LinkedBlockingQueue, queueCapacity: 100, scheduler: class org.apache.hadoop.ipc.DefaultRpcScheduler, ipcBackoff: false.
2022-12-18 01:27:30,130 INFO [Socket Reader #1 for port 0] org.apache.hadoop.ipc.Server: Starting Socket Reader #1 for port 0
2022-12-18 01:27:30,241 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.yarn.factories.impl.pb.RpcServerFactoryPBImpl: Adding protocol org.apache.hadoop.mapreduce.v2.api.MRClientProtocolPB to the server
2022-12-18 01:27:30,241 INFO [IPC Server listener on 0] org.apache.hadoop.ipc.Server: IPC Server listener on 0: starting
2022-12-18 01:27:30,241 INFO [IPC Server Responder] org.apache.hadoop.ipc.Server: IPC Server Responder: starting
2022-12-18 01:27:30,242 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.mapreduce.v2.app.client.MRClientService: Instantiated MRClientService at hadoopnode/10.0.1.4:39881
2022-12-18 01:27:30,257 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.util.log: Logging initialized @1359ms to org.eclipse.jetty.util.log.Slf4jLog
2022-12-18 01:27:30,328 WARN [Listener at 0.0.0.0/39881] org.apache.hadoop.security.authentication.server.AuthenticationFilter: Unable to initialize FileSignerSecretProvider, falling back to use random secrets. Reason: Could not read signature secret file: //hadoop-http-auth-signature-secret
2022-12-18 01:27:30,330 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.http.HttpRequestLog: Http request log for http.requests.mapreduce is not defined
2022-12-18 01:27:30,333 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.http.HttpServer2: Added global filter 'safety' (class=org.apache.hadoop.http.HttpServer2$QuotingInputFilter)
2022-12-18 01:27:30,346 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.http.HttpServer2: Added filter AM_PROXY_FILTER (class=org.apache.hadoop.yarn.server.webproxy.amfilter.AmIpFilter) to context mapreduce
2022-12-18 01:27:30,346 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.http.HttpServer2: Added filter AM_PROXY_FILTER (class=org.apache.hadoop.yarn.server.webproxy.amfilter.AmIpFilter) to context static
2022-12-18 01:27:30,541 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.yarn.webapp.WebApps: Registered webapp guice modules
2022-12-18 01:27:30,542 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.http.HttpServer2: Jetty bound to port 34323
2022-12-18 01:27:30,542 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.Server: jetty-9.4.43.v20210629; built: 2021-06-30T11:07:22.254Z; git: 526006ecfa3af7f1a27ef3a288e2bef7ea9dd7e8; jvm 1.8.0_345-b01
2022-12-18 01:27:30,556 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.session: DefaultSessionIdManager workerName=node0
2022-12-18 01:27:30,556 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.session: No SessionScavenger set, using defaults
2022-12-18 01:27:30,557 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.session: node0 Scavenging every 660000ms
2022-12-18 01:27:30,563 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.handler.ContextHandler: Started o.e.j.s.ServletContextHandler@4b54af3d{static,/static,jar:file:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar!/webapps/static,AVAILABLE}
2022-12-18 01:27:30,967 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.handler.ContextHandler: Started o.e.j.w.WebAppContext@4d09cade{mapreduce,/,file:///data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000001/tmp/jetty-0_0_0_0-34323-hadoop-yarn-common-3_3_4_jar-_-any-8456777525715043818/webapp/,AVAILABLE}{jar:file:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar!/webapps/mapreduce}
2022-12-18 01:27:30,972 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.AbstractConnector: Started ServerConnector@34e20e6b{HTTP/1.1, (http/1.1)}{0.0.0.0:34323}
2022-12-18 01:27:30,972 INFO [Listener at 0.0.0.0/39881] org.eclipse.jetty.server.Server: Started @2075ms
2022-12-18 01:27:30,972 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.yarn.webapp.WebApps: Web app mapreduce started at 34323
2022-12-18 01:27:30,974 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.speculate.DefaultSpeculator: JOB_CREATE job_1671326373437_0001
2022-12-18 01:27:30,975 INFO [Listener at 0.0.0.0/39881] org.apache.hadoop.ipc.CallQueueManager: Using callQueue: class java.util.concurrent.LinkedBlockingQueue, queueCapacity: 3000, scheduler: class org.apache.hadoop.ipc.DefaultRpcScheduler, ipcBackoff: false.
2022-12-18 01:27:30,975 INFO [Socket Reader #1 for port 0] org.apache.hadoop.ipc.Server: Starting Socket Reader #1 for port 0
2022-12-18 01:27:30,978 INFO [IPC Server Responder] org.apache.hadoop.ipc.Server: IPC Server Responder: starting
2022-12-18 01:27:30,978 INFO [IPC Server listener on 0] org.apache.hadoop.ipc.Server: IPC Server listener on 0: starting
2022-12-18 01:27:30,991 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerRequestor: nodeBlacklistingEnabled:true
2022-12-18 01:27:30,991 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerRequestor: maxTaskFailuresPerNode is 3
2022-12-18 01:27:30,991 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerRequestor: blacklistDisablePercent is 33
2022-12-18 01:27:30,993 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: 0% of the mappers will be scheduled using OPPORTUNISTIC containers
2022-12-18 01:27:31,008 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.yarn.client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at resourcemanager/10.0.1.3:8030
2022-12-18 01:27:31,068 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator: maxContainerCapability: <memory:8192, vCores:4>
2022-12-18 01:27:31,068 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator: queue: default
2022-12-18 01:27:31,070 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Upper limit on the thread pool size is 500
2022-12-18 01:27:31,070 INFO [Listener at 0.0.0.0/45261] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: The thread pool initial size is 10
2022-12-18 01:27:31,081 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: job_1671326373437_0001Job Transitioned from INITED to SETUP
2022-12-18 01:27:31,082 INFO [CommitterEvent Processor #0] org.apache.hadoop.mapreduce.v2.app.commit.CommitterEventHandler: Processing the event EventType: JOB_SETUP
2022-12-18 01:27:31,091 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: job_1671326373437_0001Job Transitioned from SETUP to RUNNING
2022-12-18 01:27:31,104 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: Resource capability of task type MAP is set to <memory:1024, vCores:1>
2022-12-18 01:27:31,105 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: task_1671326373437_0001_m_000000 Task Transitioned from NEW to SCHEDULED
2022-12-18 01:27:31,106 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: task_1671326373437_0001_m_000001 Task Transitioned from NEW to SCHEDULED
2022-12-18 01:27:31,106 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000000_0 TaskAttempt Transitioned from NEW to UNASSIGNED
2022-12-18 01:27:31,107 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000001_0 TaskAttempt Transitioned from NEW to UNASSIGNED
2022-12-18 01:27:31,107 INFO [Thread-60] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: mapResourceRequest:<memory:1024, vCores:1>
2022-12-18 01:27:31,131 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Event Writer setup for JobId: job_1671326373437_0001, File: hdfs://namenode:8020/tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job_1671326373437_0001_1.jhist
2022-12-18 01:27:32,070 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Before Scheduling: PendingReds:0 ScheduledMaps:2 ScheduledReds:0 AssignedMaps:0 AssignedReds:0 CompletedMaps:0 CompletedReds:0 ContAlloc:0 ContRel:0 HostLocal:0 RackLocal:0
2022-12-18 01:27:32,103 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerRequestor: getResources() for application_1671326373437_0001: ask=1 release= 0 newContainers=0 finishedContainers=0 resourcelimit=<memory:6144, vCores:7> knownNMs=1
2022-12-18 01:27:33,114 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Got allocated containers 1
2022-12-18 01:27:33,116 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Assigned container container_1671326373437_0001_01_000002 to attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:33,117 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: After Scheduling: PendingReds:0 ScheduledMaps:1 ScheduledReds:0 AssignedMaps:1 AssignedReds:0 CompletedMaps:0 CompletedReds:0 ContAlloc:1 ContRel:0 HostLocal:0 RackLocal:0
2022-12-18 01:27:33,158 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: The job-jar file on the remote FS is hdfs://namenode:8020/tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job.jar
2022-12-18 01:27:33,161 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: The job-conf file on the remote FS is /tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job.xml
2022-12-18 01:27:33,164 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: Adding #0 tokens and #1 secret keys for NM use for launching container
2022-12-18 01:27:33,164 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: Size of containertokens_dob is 1
2022-12-18 01:27:33,164 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: Putting shuffle token in serviceData
2022-12-18 01:27:33,188 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapred.JobConf: Task java-opts do not specify heap size. Setting task attempt jvm max heap size to -Xmx820m
2022-12-18 01:27:33,190 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000000_0 TaskAttempt Transitioned from UNASSIGNED to ASSIGNED
2022-12-18 01:27:33,193 INFO [ContainerLauncher #0] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Processing the event EventType: CONTAINER_REMOTE_LAUNCH for container container_1671326373437_0001_01_000002 taskAttempt attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:33,195 INFO [ContainerLauncher #0] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Launching attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:33,243 INFO [ContainerLauncher #0] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Shuffle port returned by ContainerManager for attempt_1671326373437_0001_m_000000_0 : 13562
2022-12-18 01:27:33,244 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: TaskAttempt: [attempt_1671326373437_0001_m_000000_0] using containerId: [container_1671326373437_0001_01_000002 on NM: [hadoopnode:36113]
2022-12-18 01:27:33,246 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000000_0 TaskAttempt Transitioned from ASSIGNED to RUNNING
2022-12-18 01:27:33,246 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.speculate.DefaultSpeculator: ATTEMPT_START task_1671326373437_0001_m_000000
2022-12-18 01:27:33,246 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: task_1671326373437_0001_m_000000 Task Transitioned from SCHEDULED to RUNNING
2022-12-18 01:27:33,914 INFO [Socket Reader #1 for port 0] SecurityLogger.org.apache.hadoop.ipc.Server: Auth successful for job_1671326373437_0001 (auth:SIMPLE) from 10.0.1.4:59964
2022-12-18 01:27:33,928 INFO [IPC Server handler 0 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: JVM with ID : jvm_1671326373437_0001_m_000002 asked for a task
2022-12-18 01:27:33,928 INFO [IPC Server handler 0 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: JVM with ID: jvm_1671326373437_0001_m_000002 given task: attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:34,120 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerRequestor: getResources() for application_1671326373437_0001: ask=1 release= 0 newContainers=1 finishedContainers=0 resourcelimit=<memory:4096, vCores:5> knownNMs=1
2022-12-18 01:27:34,120 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Got allocated containers 1
2022-12-18 01:27:34,121 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Assigned container container_1671326373437_0001_01_000003 to attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:34,121 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: After Scheduling: PendingReds:0 ScheduledMaps:0 ScheduledReds:0 AssignedMaps:2 AssignedReds:0 CompletedMaps:0 CompletedReds:0 ContAlloc:2 ContRel:0 HostLocal:0 RackLocal:0
2022-12-18 01:27:34,122 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapred.JobConf: Task java-opts do not specify heap size. Setting task attempt jvm max heap size to -Xmx820m
2022-12-18 01:27:34,122 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000001_0 TaskAttempt Transitioned from UNASSIGNED to ASSIGNED
2022-12-18 01:27:34,122 INFO [ContainerLauncher #1] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Processing the event EventType: CONTAINER_REMOTE_LAUNCH for container container_1671326373437_0001_01_000003 taskAttempt attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:34,122 INFO [ContainerLauncher #1] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Launching attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:34,129 INFO [ContainerLauncher #1] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: Shuffle port returned by ContainerManager for attempt_1671326373437_0001_m_000001_0 : 13562
2022-12-18 01:27:34,130 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: TaskAttempt: [attempt_1671326373437_0001_m_000001_0] using containerId: [container_1671326373437_0001_01_000003 on NM: [hadoopnode:36113]
2022-12-18 01:27:34,130 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000001_0 TaskAttempt Transitioned from ASSIGNED to RUNNING
2022-12-18 01:27:34,130 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.speculate.DefaultSpeculator: ATTEMPT_START task_1671326373437_0001_m_000001
2022-12-18 01:27:34,130 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: task_1671326373437_0001_m_000001 Task Transitioned from SCHEDULED to RUNNING
2022-12-18 01:27:34,772 INFO [IPC Server handler 0 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Progress of TaskAttempt attempt_1671326373437_0001_m_000000_0 is : 0.0
2022-12-18 01:27:34,833 INFO [IPC Server handler 2 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Commit-pending state update from attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:34,833 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000000_0 TaskAttempt Transitioned from RUNNING to COMMIT_PENDING
2022-12-18 01:27:34,833 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: attempt_1671326373437_0001_m_000000_0 given a go for committing the task output.
2022-12-18 01:27:34,834 INFO [IPC Server handler 1 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Commit go/no-go request from attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:34,834 INFO [IPC Server handler 1 on default port 45261] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: Result of canCommit for attempt_1671326373437_0001_m_000000_0:true
2022-12-18 01:27:34,859 INFO [IPC Server handler 3 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Progress of TaskAttempt attempt_1671326373437_0001_m_000000_0 is : 1.0
2022-12-18 01:27:34,859 INFO [Socket Reader #1 for port 0] SecurityLogger.org.apache.hadoop.ipc.Server: Auth successful for job_1671326373437_0001 (auth:SIMPLE) from 10.0.1.4:59974
2022-12-18 01:27:34,863 INFO [IPC Server handler 4 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Done acknowledgment from attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:34,865 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000000_0 TaskAttempt Transitioned from COMMIT_PENDING to SUCCESS_FINISHING_CONTAINER
2022-12-18 01:27:34,867 INFO [IPC Server handler 5 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: JVM with ID : jvm_1671326373437_0001_m_000003 asked for a task
2022-12-18 01:27:34,867 INFO [IPC Server handler 5 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: JVM with ID: jvm_1671326373437_0001_m_000003 given task: attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:34,870 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: Task succeeded with attempt attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:34,871 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: task_1671326373437_0001_m_000000 Task Transitioned from RUNNING to SUCCEEDED
2022-12-18 01:27:34,872 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Num completed Tasks: 1
2022-12-18 01:27:35,121 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Before Scheduling: PendingReds:0 ScheduledMaps:0 ScheduledReds:0 AssignedMaps:2 AssignedReds:0 CompletedMaps:1 CompletedReds:0 ContAlloc:2 ContRel:0 HostLocal:0 RackLocal:0
2022-12-18 01:27:35,124 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerRequestor: getResources() for application_1671326373437_0001: ask=1 release= 0 newContainers=1 finishedContainers=0 resourcelimit=<memory:3072, vCores:4> knownNMs=1
2022-12-18 01:27:35,124 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Got allocated containers 1
2022-12-18 01:27:35,124 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Cannot assign container Container: [ContainerId: container_1671326373437_0001_01_000004, AllocationRequestId: -1, Version: 0, NodeId: hadoopnode:36113, NodeHttpAddress: hadoopnode:8042, Resource: <memory:1024, vCores:1>, Priority: 20, Token: Token { kind: ContainerToken, service: 10.0.1.4:36113 }, ExecutionType: GUARANTEED, ] for a map as either  container memory less than required <memory:1024, vCores:1> or no pending map tasks - maps.isEmpty=true
2022-12-18 01:27:35,125 INFO [RMCommunicator Allocator] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: After Scheduling: PendingReds:0 ScheduledMaps:0 ScheduledReds:0 AssignedMaps:2 AssignedReds:0 CompletedMaps:1 CompletedReds:0 ContAlloc:3 ContRel:1 HostLocal:0 RackLocal:0
2022-12-18 01:27:35,634 INFO [IPC Server handler 0 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Progress of TaskAttempt attempt_1671326373437_0001_m_000001_0 is : 0.0
2022-12-18 01:27:35,688 INFO [IPC Server handler 2 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Commit-pending state update from attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:35,688 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000001_0 TaskAttempt Transitioned from RUNNING to COMMIT_PENDING
2022-12-18 01:27:35,688 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: attempt_1671326373437_0001_m_000001_0 given a go for committing the task output.
2022-12-18 01:27:35,689 INFO [IPC Server handler 1 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Commit go/no-go request from attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:35,689 INFO [IPC Server handler 1 on default port 45261] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: Result of canCommit for attempt_1671326373437_0001_m_000001_0:true
2022-12-18 01:27:35,700 INFO [IPC Server handler 3 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Progress of TaskAttempt attempt_1671326373437_0001_m_000001_0 is : 1.0
2022-12-18 01:27:35,701 INFO [IPC Server handler 4 on default port 45261] org.apache.hadoop.mapred.TaskAttemptListenerImpl: Done acknowledgment from attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:35,702 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000001_0 TaskAttempt Transitioned from COMMIT_PENDING to SUCCESS_FINISHING_CONTAINER
2022-12-18 01:27:35,702 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: Task succeeded with attempt attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:35,702 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl: task_1671326373437_0001_m_000001 Task Transitioned from RUNNING to SUCCEEDED
2022-12-18 01:27:35,702 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Num completed Tasks: 2
2022-12-18 01:27:35,703 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: job_1671326373437_0001Job Transitioned from RUNNING to COMMITTING
2022-12-18 01:27:35,703 INFO [CommitterEvent Processor #1] org.apache.hadoop.mapreduce.v2.app.commit.CommitterEventHandler: Processing the event EventType: JOB_COMMIT
2022-12-18 01:27:35,727 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: Calling handler for JobFinishedEvent 
2022-12-18 01:27:35,727 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.JobImpl: job_1671326373437_0001Job Transitioned from COMMITTING to SUCCEEDED
2022-12-18 01:27:35,728 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Job finished cleanly, recording last MRAppMaster retry
2022-12-18 01:27:35,728 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Notify RMCommunicator isAMLastRetry: true
2022-12-18 01:27:35,728 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator: RMCommunicator notified that shouldUnregistered is: true
2022-12-18 01:27:35,728 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Notify JHEH isAMLastRetry: true
2022-12-18 01:27:35,728 INFO [Thread-75] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: JobHistoryEventHandler notified that forceJobCompletion is true
2022-12-18 01:27:35,728 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Calling stop for all the services
2022-12-18 01:27:35,729 INFO [Thread-75] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Stopping JobHistoryEventHandler. Size of the outstanding queue size is 0
2022-12-18 01:27:35,750 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Copying hdfs://namenode:8020/tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job_1671326373437_0001_1.jhist to hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001-1671326847669-sandbox-TeraGen-1671326855725-2-0-SUCCEEDED-default-1671326851073.jhist_tmp
2022-12-18 01:27:35,771 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Copied from: hdfs://namenode:8020/tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job_1671326373437_0001_1.jhist to done location: hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001-1671326847669-sandbox-TeraGen-1671326855725-2-0-SUCCEEDED-default-1671326851073.jhist_tmp
2022-12-18 01:27:35,772 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Set historyUrl to http://jobhistoryserver:19888/jobhistory/job/job_1671326373437_0001
2022-12-18 01:27:35,773 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Copying hdfs://namenode:8020/tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job_1671326373437_0001_1_conf.xml to hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001_conf.xml_tmp
2022-12-18 01:27:35,790 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Copied from: hdfs://namenode:8020/tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001/job_1671326373437_0001_1_conf.xml to done location: hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001_conf.xml_tmp
2022-12-18 01:27:35,795 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Moved tmp to done: hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001.summary_tmp to hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001.summary
2022-12-18 01:27:35,797 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Moved tmp to done: hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001_conf.xml_tmp to hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001_conf.xml
2022-12-18 01:27:35,798 INFO [eventHandlingThread] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Moved tmp to done: hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001-1671326847669-sandbox-TeraGen-1671326855725-2-0-SUCCEEDED-default-1671326851073.jhist_tmp to hdfs://namenode:8020/mr-history/tmp/sandbox/job_1671326373437_0001-1671326847669-sandbox-TeraGen-1671326855725-2-0-SUCCEEDED-default-1671326851073.jhist
2022-12-18 01:27:35,799 INFO [Thread-75] org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler: Stopped JobHistoryEventHandler. super.stop()
2022-12-18 01:27:35,799 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: KILLING attempt_1671326373437_0001_m_000001_0
2022-12-18 01:27:35,821 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.launcher.ContainerLauncherImpl: KILLING attempt_1671326373437_0001_m_000000_0
2022-12-18 01:27:35,821 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000001_0 TaskAttempt Transitioned from SUCCESS_FINISHING_CONTAINER to SUCCEEDED
2022-12-18 01:27:35,827 INFO [AsyncDispatcher event handler] org.apache.hadoop.mapreduce.v2.app.job.impl.TaskAttemptImpl: attempt_1671326373437_0001_m_000000_0 TaskAttempt Transitioned from SUCCESS_FINISHING_CONTAINER to SUCCEEDED
2022-12-18 01:27:35,828 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator: Setting job diagnostics to 
2022-12-18 01:27:35,828 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator: History url is http://jobhistoryserver:19888/jobhistory/job/job_1671326373437_0001
2022-12-18 01:27:35,840 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.rm.RMCommunicator: Waiting for application to be successfully unregistered.
2022-12-18 01:27:36,841 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator: Final Stats: PendingReds:0 ScheduledMaps:0 ScheduledReds:0 AssignedMaps:2 AssignedReds:0 CompletedMaps:1 CompletedReds:0 ContAlloc:3 ContRel:1 HostLocal:0 RackLocal:0
2022-12-18 01:27:36,842 INFO [Thread-75] org.apache.hadoop.mapreduce.v2.app.MRAppMaster: Deleting staging directory hdfs://namenode:8020 /tmp/hadoop-yarn/staging/sandbox/.staging/job_1671326373437_0001
2022-12-18 01:27:36,849 INFO [Thread-75] org.apache.hadoop.ipc.Server: Stopping server on 45261
2022-12-18 01:27:36,850 INFO [IPC Server listener on 0] org.apache.hadoop.ipc.Server: Stopping IPC Server listener on 0
2022-12-18 01:27:36,850 INFO [IPC Server Responder] org.apache.hadoop.ipc.Server: Stopping IPC Server Responder
2022-12-18 01:27:36,850 INFO [TaskHeartbeatHandler PingChecker] org.apache.hadoop.mapreduce.v2.app.TaskHeartbeatHandler: TaskHeartbeatHandler thread interrupted
2022-12-18 01:27:36,851 INFO [Ping Checker for TaskAttemptFinishingMonitor] org.apache.hadoop.yarn.util.AbstractLivelinessMonitor: TaskAttemptFinishingMonitor thread interrupted
2022-12-18 01:27:41,851 INFO [Thread-75] org.apache.hadoop.ipc.Server: Stopping server on 39881
2022-12-18 01:27:41,851 INFO [IPC Server listener on 0] org.apache.hadoop.ipc.Server: Stopping IPC Server listener on 0
2022-12-18 01:27:41,851 INFO [IPC Server Responder] org.apache.hadoop.ipc.Server: Stopping IPC Server Responder
2022-12-18 01:27:41,853 INFO [Thread-75] org.eclipse.jetty.server.handler.ContextHandler: Stopped o.e.j.w.WebAppContext@4d09cade{mapreduce,/,null,STOPPED}{jar:file:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar!/webapps/mapreduce}
2022-12-18 01:27:41,857 INFO [Thread-75] org.eclipse.jetty.server.AbstractConnector: Stopped ServerConnector@34e20e6b{HTTP/1.1, (http/1.1)}{0.0.0.0:0}
2022-12-18 01:27:41,857 INFO [Thread-75] org.eclipse.jetty.server.session: node0 Stopped scavenging
2022-12-18 01:27:41,857 INFO [Thread-75] org.eclipse.jetty.server.handler.ContextHandler: Stopped o.e.j.s.ServletContextHandler@4b54af3d{static,/static,jar:file:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar!/webapps/static,STOPPED}
""",
        },
        "container_1671326373437_0001_01_000002": {
            "directory.info": b"""ls -l:
total 32
-rw-r--r-- 1 yarn yarn  129 Dec 18 01:27 container_tokens
-rwx------ 1 yarn yarn  627 Dec 18 01:27 default_container_executor_session.sh
-rwx------ 1 yarn yarn  682 Dec 18 01:27 default_container_executor.sh
lrwxrwxrwx 1 yarn yarn   97 Dec 18 01:27 job.jar -> /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/11/job.jar
lrwxrwxrwx 1 yarn yarn   97 Dec 18 01:27 job.xml -> /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/13/job.xml
-rwx------ 1 yarn yarn 4932 Dec 18 01:27 launch_container.sh
drwx--x--- 2 yarn yarn 4096 Dec 18 01:27 tmp
find -L . -maxdepth 5 -ls:
 63318156      4 drwx--x---   3 yarn     yarn         4096 Dec 18 01:27 .
 63318158      4 drwx--x---   2 yarn     yarn         4096 Dec 18 01:27 ./tmp
 63318165      4 -rwx------   1 yarn     yarn          682 Dec 18 01:27 ./default_container_executor.sh
 63318163      4 -rwx------   1 yarn     yarn          627 Dec 18 01:27 ./default_container_executor_session.sh
 63318162      4 -rw-r--r--   1 yarn     yarn           48 Dec 18 01:27 ./.launch_container.sh.crc
 63317898      4 drwx------   2 yarn     yarn         4096 Dec 18 01:27 ./job.jar
 63317919    276 -r-x------   1 yarn     yarn       280992 Dec 18 01:27 ./job.jar/job.jar
 63318164      4 -rw-r--r--   1 yarn     yarn           16 Dec 18 01:27 ./.default_container_executor_session.sh.crc
 63318115    232 -r-x------   1 yarn     yarn       235968 Dec 18 01:27 ./job.xml
 63318159      4 -rw-r--r--   1 yarn     yarn          129 Dec 18 01:27 ./container_tokens
 63318161      8 -rwx------   1 yarn     yarn         4932 Dec 18 01:27 ./launch_container.sh
 63318160      4 -rw-r--r--   1 yarn     yarn           12 Dec 18 01:27 ./.container_tokens.crc
 63318166      4 -rw-r--r--   1 yarn     yarn           16 Dec 18 01:27 ./.default_container_executor.sh.crc
broken symlinks(find -L . -maxdepth 5 -type l -ls):
""",
            "launch_container.sh": b"""#!/bin/bash

set -o pipefail -e
export PRELAUNCH_OUT="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/prelaunch.out"
exec >"${PRELAUNCH_OUT}"
export PRELAUNCH_ERR="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/prelaunch.err"
exec 2>"${PRELAUNCH_ERR}"
echo "Setting up env variables"
export JAVA_HOME=${JAVA_HOME:-"/opt/java/openjdk"}
export HADOOP_COMMON_HOME=${HADOOP_COMMON_HOME:-"/hadoop"}
export HADOOP_HDFS_HOME=${HADOOP_HDFS_HOME:-"/hadoop"}
export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/hadoop/etc/hadoop"}
export HADOOP_YARN_HOME=${HADOOP_YARN_HOME:-"/hadoop"}
export HADOOP_HOME=${HADOOP_HOME:-"/hadoop"}
export PATH=${PATH:-"/hadoop/bin:/hadoop/sbin:/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"}
export LANG=${LANG:-"en_US.UTF-8"}
export HADOOP_MAPRED_HOME=${HADOOP_MAPRED_HOME:-"/hadoop"}
export HADOOP_TOKEN_FILE_LOCATION="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000002/container_tokens"
export CONTAINER_ID="container_1671326373437_0001_01_000002"
export NM_PORT="36113"
export NM_HOST="hadoopnode"
export NM_HTTP_PORT="8042"
export LOCAL_DIRS="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001"
export LOCAL_USER_DIRS="/data/nm-local-dir/usercache/sandbox/"
export LOG_DIRS="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002"
export USER="sandbox"
export LOGNAME="sandbox"
export HOME="/home/"
export PWD="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000002"
export LOCALIZATION_COUNTERS="0,518812,0,2,3"
export JVM_PID="$$"
export NM_AUX_SERVICE_mapreduce_shuffle="AAA0+gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
export STDOUT_LOGFILE_ENV="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/stdout"
export SHELL="/bin/bash"
export HADOOP_ROOT_LOGGER="INFO,console"
export CLASSPATH="$PWD:$HADOOP_CONF_DIR:$HADOOP_COMMON_HOME/share/hadoop/common/*:$HADOOP_COMMON_HOME/share/hadoop/common/lib/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/lib/*:$HADOOP_YARN_HOME/share/hadoop/yarn/*:$HADOOP_YARN_HOME/share/hadoop/yarn/lib/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*:job.jar/*:job.jar/classes/:job.jar/lib/*:$PWD/*"
export LD_LIBRARY_PATH="$PWD:$HADOOP_COMMON_HOME/lib/native"
export STDERR_LOGFILE_ENV="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/stderr"
export HADOOP_CLIENT_OPTS=""
export MALLOC_ARENA_MAX="4"
echo "Setting up job resources"
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/11/job.jar" "job.jar"
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/13/job.xml" "job.xml"
echo "Copying debugging information"
# Creating copy of launch script
cp "launch_container.sh" "/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/launch_container.sh"
chmod 640 "/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/launch_container.sh"
# Determining directory contents
echo "ls -l:" 1>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/directory.info"
ls -l 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/directory.info"
echo "find -L . -maxdepth 5 -ls:" 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/directory.info"
find -L . -maxdepth 5 -ls 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/directory.info"
echo "broken symlinks(find -L . -maxdepth 5 -type l -ls):" 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/directory.info"
find -L . -maxdepth 5 -type l -ls 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/directory.info"
echo "Launching container"
exec /bin/bash -c "$JAVA_HOME/bin/java -Djava.net.preferIPv4Stack=true -Dhadoop.metrics.log.level=WARN   -Xmx820m -Djava.io.tmpdir=$PWD/tmp -Dlog4j.configuration=container-log4j.properties -Dyarn.app.container.log.dir=/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002 -Dyarn.app.container.log.filesize=0 -Dhadoop.root.logger=INFO,CLA -Dhadoop.root.logfile=syslog org.apache.hadoop.mapred.YarnChild 10.0.1.4 45261 attempt_1671326373437_0001_m_000000_0 2 1>/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/stdout 2>/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000002/stderr "
""",
            "prelaunch.err": b"""""",
            "prelaunch.out": b"""Setting up env variables
Setting up job resources
Copying debugging information
Launching container
""",
            "stderr": b"""""",
            "stdout": b"""""",
            "syslog": b"""2022-12-18 01:27:33,739 INFO [main] org.apache.hadoop.security.SecurityUtil: Updating Configuration
2022-12-18 01:27:33,782 INFO [main] org.apache.hadoop.metrics2.impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2022-12-18 01:27:33,823 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 second(s).
2022-12-18 01:27:33,823 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MapTask metrics system started
2022-12-18 01:27:33,850 INFO [main] org.apache.hadoop.mapred.YarnChild: Executing with tokens: [Kind: mapreduce.job, Service: job_1671326373437_0001, Ident: (org.apache.hadoop.mapreduce.security.token.JobTokenIdentifier@1ebd319f)]
2022-12-18 01:27:33,867 INFO [main] org.apache.hadoop.mapred.YarnChild: Sleeping for 0ms before retrying again. Got null now.
2022-12-18 01:27:33,975 INFO [main] org.apache.hadoop.mapred.YarnChild: mapreduce.cluster.local.dir for child: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001
2022-12-18 01:27:34,110 INFO [main] org.apache.hadoop.mapred.YarnChild: 
/************************************************************
[system properties]
os.name: Linux
os.version: 6.0.0-6-amd64
java.home: /opt/java/openjdk/jre
java.runtime.version: 1.8.0_345-b01
java.vendor: Temurin
java.version: 1.8.0_345
java.vm.name: OpenJDK 64-Bit Server VM
java.class.path: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000002:/hadoop/etc/hadoop:/hadoop/share/hadoop/common/hadoop-nfs-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-kms-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-registry-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-common-3.3.4-tests.jar:/hadoop/share/hadoop/common/hadoop-common-3.3.4.jar:/hadoop/share/hadoop/common/lib/kerby-pkix-1.0.1.jar:/hadoop/share/hadoop/common/lib/nimbus-jose-jwt-9.8.1.jar:/hadoop/share/hadoop/common/lib/jetty-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/asm-5.0.4.jar:/hadoop/share/hadoop/common/lib/paranamer-2.3.jar:/hadoop/share/hadoop/common/lib/commons-configuration2-2.1.1.jar:/hadoop/share/hadoop/common/lib/kerb-identity-1.0.1.jar:/hadoop/share/hadoop/common/lib/re2j-1.1.jar:/hadoop/share/hadoop/common/lib/jackson-xc-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-beanutils-1.9.4.jar:/hadoop/share/hadoop/common/lib/jsch-0.1.55.jar:/hadoop/share/hadoop/common/lib/commons-math3-3.1.1.jar:/hadoop/share/hadoop/common/lib/jackson-mapper-asl-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-security-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-codec-1.15.jar:/hadoop/share/hadoop/common/lib/gson-2.8.9.jar:/hadoop/share/hadoop/common/lib/j2objc-annotations-1.1.jar:/hadoop/share/hadoop/common/lib/jackson-core-asl-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-webapp-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/animal-sniffer-annotations-1.17.jar:/hadoop/share/hadoop/common/lib/jackson-jaxrs-1.9.13.jar:/hadoop/share/hadoop/common/lib/kerby-util-1.0.1.jar:/hadoop/share/hadoop/common/lib/zookeeper-3.5.6.jar:/hadoop/share/hadoop/common/lib/accessors-smart-2.4.7.jar:/hadoop/share/hadoop/common/lib/reload4j-1.2.22.jar:/hadoop/share/hadoop/common/lib/jcip-annotations-1.0-1.jar:/hadoop/share/hadoop/common/lib/jersey-servlet-1.19.jar:/hadoop/share/hadoop/common/lib/metrics-core-3.2.4.jar:/hadoop/share/hadoop/common/lib/jersey-json-1.19.jar:/hadoop/share/hadoop/common/lib/jsp-api-2.1.jar:/hadoop/share/hadoop/common/lib/curator-client-4.2.0.jar:/hadoop/share/hadoop/common/lib/curator-recipes-4.2.0.jar:/hadoop/share/hadoop/common/lib/commons-text-1.4.jar:/hadoop/share/hadoop/common/lib/jersey-server-1.19.jar:/hadoop/share/hadoop/common/lib/kerb-simplekdc-1.0.1.jar:/hadoop/share/hadoop/common/lib/jersey-core-1.19.jar:/hadoop/share/hadoop/common/lib/avro-1.7.7.jar:/hadoop/share/hadoop/common/lib/commons-io-2.8.0.jar:/hadoop/share/hadoop/common/lib/kerb-core-1.0.1.jar:/hadoop/share/hadoop/common/lib/slf4j-api-1.7.36.jar:/hadoop/share/hadoop/common/lib/kerb-server-1.0.1.jar:/hadoop/share/hadoop/common/lib/commons-collections-3.2.2.jar:/hadoop/share/hadoop/common/lib/jackson-core-2.12.7.jar:/hadoop/share/hadoop/common/lib/commons-daemon-1.0.13.jar:/hadoop/share/hadoop/common/lib/snappy-java-1.1.8.2.jar:/hadoop/share/hadoop/common/lib/jettison-1.1.jar:/hadoop/share/hadoop/common/lib/kerb-common-1.0.1.jar:/hadoop/share/hadoop/common/lib/jetty-http-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/failureaccess-1.0.jar:/hadoop/share/hadoop/common/lib/jul-to-slf4j-1.7.36.jar:/hadoop/share/hadoop/common/lib/jaxb-api-2.2.11.jar:/hadoop/share/hadoop/common/lib/jsr311-api-1.1.1.jar:/hadoop/share/hadoop/common/lib/jaxb-impl-2.2.3-1.jar:/hadoop/share/hadoop/common/lib/javax.servlet-api-3.1.0.jar:/hadoop/share/hadoop/common/lib/zookeeper-jute-3.5.6.jar:/hadoop/share/hadoop/common/lib/jetty-util-ajax-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-compress-1.21.jar:/hadoop/share/hadoop/common/lib/commons-net-3.6.jar:/hadoop/share/hadoop/common/lib/commons-cli-1.2.jar:/hadoop/share/hadoop/common/lib/checker-qual-2.5.2.jar:/hadoop/share/hadoop/common/lib/jetty-io-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/netty-3.10.6.Final.jar:/hadoop/share/hadoop/common/lib/kerb-crypto-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerby-asn1-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerby-xdr-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerb-util-1.0.1.jar:/hadoop/share/hadoop/common/lib/commons-logging-1.1.3.jar:/hadoop/share/hadoop/common/lib/commons-lang3-3.12.0.jar:/hadoop/share/hadoop/common/lib/token-provider-1.0.1.jar:/hadoop/share/hadoop/common/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/hadoop/share/hadoop/common/lib/jakarta.activation-api-1.2.1.jar:/hadoop/share/hadoop/common/lib/httpclient-4.5.13.jar:/hadoop/share/hadoop/common/lib/hadoop-shaded-guava-1.1.1.jar:/hadoop/share/hadoop/common/lib/hadoop-annotations-3.3.4.jar:/hadoop/share/hadoop/common/lib/hadoop-auth-3.3.4.jar:/hadoop/share/hadoop/common/lib/jackson-databind-2.12.7.jar:/hadoop/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar:/hadoop/share/hadoop/common/lib/curator-framework-4.2.0.jar:/hadoop/share/hadoop/common/lib/woodstox-core-5.3.0.jar:/hadoop/share/hadoop/common/lib/audience-annotations-0.5.0.jar:/hadoop/share/hadoop/common/lib/kerb-client-1.0.1.jar:/hadoop/share/hadoop/common/lib/json-smart-2.4.7.jar:/hadoop/share/hadoop/common/lib/dnsjava-2.1.7.jar:/hadoop/share/hadoop/common/lib/jsr305-3.0.2.jar:/hadoop/share/hadoop/common/lib/kerb-admin-1.0.1.jar:/hadoop/share/hadoop/common/lib/httpcore-4.4.13.jar:/hadoop/share/hadoop/common/lib/protobuf-java-2.5.0.jar:/hadoop/share/hadoop/common/lib/kerby-config-1.0.1.jar:/hadoop/share/hadoop/common/lib/jetty-util-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/jackson-annotations-2.12.7.jar:/hadoop/share/hadoop/common/lib/jetty-xml-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/hadoop-shaded-protobuf_3_7-1.1.1.jar:/hadoop/share/hadoop/common/lib/stax2-api-4.2.1.jar:/hadoop/share/hadoop/common/lib/guava-27.0-jre.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-native-client-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-rbf-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-rbf-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-native-client-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-httpfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-client-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-client-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-nfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/kerby-pkix-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/nimbus-jose-jwt-9.8.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/asm-5.0.4.jar:/hadoop/share/hadoop/hdfs/lib/paranamer-2.3.jar:/hadoop/share/hadoop/hdfs/lib/commons-configuration2-2.1.1.jar:/hadoop/share/hadoop/hdfs/lib/kerb-identity-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/re2j-1.1.jar:/hadoop/share/hadoop/hdfs/lib/jackson-xc-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/jetty-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-beanutils-1.9.4.jar:/hadoop/share/hadoop/hdfs/lib/leveldbjni-all-1.8.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-dns-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-rxtx-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jsch-0.1.55.jar:/hadoop/share/hadoop/hdfs/lib/commons-math3-3.1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-http2-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-udt-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jackson-mapper-asl-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/okhttp-4.9.3.jar:/hadoop/share/hadoop/hdfs/lib/jetty-security-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/commons-codec-1.15.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-mqtt-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-native-macos-4.1.77.Final-osx-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/gson-2.8.9.jar:/hadoop/share/hadoop/hdfs/lib/j2objc-annotations-1.1.jar:/hadoop/share/hadoop/hdfs/lib/jackson-core-asl-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/jetty-webapp-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/animal-sniffer-annotations-1.17.jar:/hadoop/share/hadoop/hdfs/lib/okio-2.8.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-handler-proxy-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jackson-jaxrs-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/kerby-util-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/zookeeper-3.5.6.jar:/hadoop/share/hadoop/hdfs/lib/accessors-smart-2.4.7.jar:/hadoop/share/hadoop/hdfs/lib/reload4j-1.2.22.jar:/hadoop/share/hadoop/hdfs/lib/jcip-annotations-1.0-1.jar:/hadoop/share/hadoop/hdfs/lib/jersey-servlet-1.19.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-kqueue-4.1.77.Final-osx-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/jersey-json-1.19.jar:/hadoop/share/hadoop/hdfs/lib/curator-client-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/curator-recipes-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/commons-text-1.4.jar:/hadoop/share/hadoop/hdfs/lib/kotlin-stdlib-common-1.4.10.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-unix-common-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-all-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-epoll-4.1.77.Final-linux-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/jersey-server-1.19.jar:/hadoop/share/hadoop/hdfs/lib/netty-common-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-simplekdc-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jersey-core-1.19.jar:/hadoop/share/hadoop/hdfs/lib/avro-1.7.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-io-2.8.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-haproxy-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-core-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-sctp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-server-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/commons-collections-3.2.2.jar:/hadoop/share/hadoop/hdfs/lib/jackson-core-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-http-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-daemon-1.0.13.jar:/hadoop/share/hadoop/hdfs/lib/snappy-java-1.1.8.2.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-classes-epoll-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jettison-1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-smtp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-common-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-http-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/failureaccess-1.0.jar:/hadoop/share/hadoop/hdfs/lib/kotlin-stdlib-1.4.10.jar:/hadoop/share/hadoop/hdfs/lib/jaxb-api-2.2.11.jar:/hadoop/share/hadoop/hdfs/lib/netty-buffer-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-classes-macos-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jsr311-api-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/json-simple-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-stomp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jaxb-impl-2.2.3-1.jar:/hadoop/share/hadoop/hdfs/lib/javax.servlet-api-3.1.0.jar:/hadoop/share/hadoop/hdfs/lib/zookeeper-jute-3.5.6.jar:/hadoop/share/hadoop/hdfs/lib/jetty-util-ajax-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-epoll-4.1.77.Final-linux-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/netty-handler-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-compress-1.21.jar:/hadoop/share/hadoop/hdfs/lib/commons-net-3.6.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-xml-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-cli-1.2.jar:/hadoop/share/hadoop/hdfs/lib/checker-qual-2.5.2.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-kqueue-4.1.77.Final-osx-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-memcache-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jetty-io-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-3.10.6.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-crypto-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerby-asn1-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerby-xdr-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerb-util-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/commons-logging-1.1.3.jar:/hadoop/share/hadoop/hdfs/lib/commons-lang3-3.12.0.jar:/hadoop/share/hadoop/hdfs/lib/token-provider-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/hadoop/share/hadoop/hdfs/lib/jakarta.activation-api-1.2.1.jar:/hadoop/share/hadoop/hdfs/lib/httpclient-4.5.13.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-redis-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-shaded-guava-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-annotations-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-auth-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/jackson-databind-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/curator-framework-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-native-macos-4.1.77.Final-osx-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/woodstox-core-5.3.0.jar:/hadoop/share/hadoop/hdfs/lib/audience-annotations-0.5.0.jar:/hadoop/share/hadoop/hdfs/lib/kerb-client-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/json-smart-2.4.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-socks-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-classes-kqueue-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/dnsjava-2.1.7.jar:/hadoop/share/hadoop/hdfs/lib/jsr305-3.0.2.jar:/hadoop/share/hadoop/hdfs/lib/kerb-admin-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/httpcore-4.4.13.jar:/hadoop/share/hadoop/hdfs/lib/protobuf-java-2.5.0.jar:/hadoop/share/hadoop/hdfs/lib/kerby-config-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-util-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/jackson-annotations-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/jetty-xml-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-shaded-protobuf_3_7-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/stax2-api-4.2.1.jar:/hadoop/share/hadoop/hdfs/lib/guava-27.0-jre.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-registry-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-router-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-client-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-distributedshell-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-services-core-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-nodemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-api-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-resourcemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-mawo-core-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-services-api-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-tests-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-unmanaged-am-launcher-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-sharedcachemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-web-proxy-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-timeline-pluginstorage-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-applicationhistoryservice-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-common-3.3.4.jar:/hadoop/share/hadoop/yarn/lib/javax.websocket-api-1.0.jar:/hadoop/share/hadoop/yarn/lib/websocket-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/json-io-2.5.1.jar:/hadoop/share/hadoop/yarn/lib/jline-3.9.0.jar:/hadoop/share/hadoop/yarn/lib/bcprov-jdk15on-1.60.jar:/hadoop/share/hadoop/yarn/lib/websocket-common-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jetty-jndi-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/websocket-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jackson-module-jaxb-annotations-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/HikariCP-java7-2.4.12.jar:/hadoop/share/hadoop/yarn/lib/jersey-client-1.19.jar:/hadoop/share/hadoop/yarn/lib/metrics-core-3.2.4.jar:/hadoop/share/hadoop/yarn/lib/jetty-client-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/guice-servlet-4.0.jar:/hadoop/share/hadoop/yarn/lib/swagger-annotations-1.5.4.jar:/hadoop/share/hadoop/yarn/lib/bcpkix-jdk15on-1.60.jar:/hadoop/share/hadoop/yarn/lib/websocket-api-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jna-5.2.0.jar:/hadoop/share/hadoop/yarn/lib/jackson-jaxrs-base-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/javax-websocket-client-impl-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/snakeyaml-1.26.jar:/hadoop/share/hadoop/yarn/lib/asm-tree-9.1.jar:/hadoop/share/hadoop/yarn/lib/javax.websocket-client-api-1.0.jar:/hadoop/share/hadoop/yarn/lib/javax-websocket-server-impl-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jackson-jaxrs-json-provider-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/asm-analysis-9.1.jar:/hadoop/share/hadoop/yarn/lib/websocket-client-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/ehcache-3.3.1.jar:/hadoop/share/hadoop/yarn/lib/guice-4.0.jar:/hadoop/share/hadoop/yarn/lib/fst-2.50.jar:/hadoop/share/hadoop/yarn/lib/jetty-plus-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jetty-annotations-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/geronimo-jcache_1.0_spec-1.0-alpha-1.jar:/hadoop/share/hadoop/yarn/lib/mssql-jdbc-6.2.1.jre7.jar:/hadoop/share/hadoop/yarn/lib/objenesis-2.6.jar:/hadoop/share/hadoop/yarn/lib/jersey-guice-1.19.jar:/hadoop/share/hadoop/yarn/lib/jakarta.xml.bind-api-2.3.2.jar:/hadoop/share/hadoop/yarn/lib/aopalliance-1.0.jar:/hadoop/share/hadoop/yarn/lib/javax.inject-1.jar:/hadoop/share/hadoop/yarn/lib/asm-commons-9.1.jar:/hadoop/share/hadoop/yarn/lib/java-util-1.9.0.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-plugins-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-shuffle-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.4-tests.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-nativetask-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-app-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-uploader-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.3.4.jar:/hadoop/share/hadoop/mapreduce/lib/*:job.jar/job.jar:job.jar/classes/:job.jar/lib/*:/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000002/job.jar
java.io.tmpdir: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000002/tmp
user.dir: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000002
user.name: yarn
************************************************************/
2022-12-18 01:27:34,110 INFO [main] org.apache.hadoop.conf.Configuration.deprecation: session.id is deprecated. Instead, use dfs.metrics.session-id
2022-12-18 01:27:34,336 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: File Output Committer Algorithm version is 2
2022-12-18 01:27:34,336 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2022-12-18 01:27:34,344 INFO [main] org.apache.hadoop.mapred.Task:  Using ResourceCalculatorProcessTree : [ ]
2022-12-18 01:27:34,421 INFO [main] org.apache.hadoop.mapred.MapTask: Processing split: org.apache.hadoop.examples.terasort.TeraGen$RangeInputFormat$RangeInputSplit@46f699d5
2022-12-18 01:27:34,828 INFO [main] org.apache.hadoop.mapred.Task: Task:attempt_1671326373437_0001_m_000000_0 is done. And is in the process of committing
2022-12-18 01:27:34,835 INFO [main] org.apache.hadoop.mapred.Task: Task attempt_1671326373437_0001_m_000000_0 is allowed to commit now
2022-12-18 01:27:34,853 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: Saved output of task 'attempt_1671326373437_0001_m_000000_0' to hdfs://namenode:8020/user/sandbox/teragen
2022-12-18 01:27:34,864 INFO [main] org.apache.hadoop.mapred.Task: Task 'attempt_1671326373437_0001_m_000000_0' done.
2022-12-18 01:27:34,868 INFO [main] org.apache.hadoop.mapred.Task: Final Counters for attempt_1671326373437_0001_m_000000_0: Counters: 27
	File System Counters
		FILE: Number of bytes read=0
		FILE: Number of bytes written=275762
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=82
		HDFS: Number of bytes written=50000000
		HDFS: Number of read operations=6
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Map-Reduce Framework
		Map input records=500000
		Map output records=500000
		Input split bytes=82
		Spilled Records=0
		Failed Shuffles=0
		Merged Map outputs=0
		GC time elapsed (ms)=31
		CPU time spent (ms)=1650
		Physical memory (bytes) snapshot=384585728
		Virtual memory (bytes) snapshot=2617733120
		Total committed heap usage (bytes)=603979776
		Peak Map Physical memory (bytes)=384585728
		Peak Map Virtual memory (bytes)=2617733120
	org.apache.hadoop.examples.terasort.TeraGen$Counters
		CHECKSUM=1074598070305752
	File Input Format Counters 
		Bytes Read=0
	File Output Format Counters 
		Bytes Written=50000000
2022-12-18 01:27:34,869 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: Stopping MapTask metrics system...
2022-12-18 01:27:34,869 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MapTask metrics system stopped.
2022-12-18 01:27:34,869 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MapTask metrics system shutdown complete.
""",
        },
        "container_1671326373437_0001_01_000003": {
            "directory.info": b"""ls -l:
total 32
-rw-r--r-- 1 yarn yarn  129 Dec 18 01:27 container_tokens
-rwx------ 1 yarn yarn  627 Dec 18 01:27 default_container_executor_session.sh
-rwx------ 1 yarn yarn  682 Dec 18 01:27 default_container_executor.sh
lrwxrwxrwx 1 yarn yarn   97 Dec 18 01:27 job.jar -> /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/11/job.jar
lrwxrwxrwx 1 yarn yarn   97 Dec 18 01:27 job.xml -> /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/13/job.xml
-rwx------ 1 yarn yarn 4932 Dec 18 01:27 launch_container.sh
drwx--x--- 2 yarn yarn 4096 Dec 18 01:27 tmp
find -L . -maxdepth 5 -ls:
 63318185      4 drwx--x---   3 yarn     yarn         4096 Dec 18 01:27 .
 63318187      4 drwx--x---   2 yarn     yarn         4096 Dec 18 01:27 ./tmp
 63318194      4 -rwx------   1 yarn     yarn          682 Dec 18 01:27 ./default_container_executor.sh
 63318192      4 -rwx------   1 yarn     yarn          627 Dec 18 01:27 ./default_container_executor_session.sh
 63318191      4 -rw-r--r--   1 yarn     yarn           48 Dec 18 01:27 ./.launch_container.sh.crc
 63317898      4 drwx------   2 yarn     yarn         4096 Dec 18 01:27 ./job.jar
 63317919    276 -r-x------   1 yarn     yarn       280992 Dec 18 01:27 ./job.jar/job.jar
 63318193      4 -rw-r--r--   1 yarn     yarn           16 Dec 18 01:27 ./.default_container_executor_session.sh.crc
 63318115    232 -r-x------   1 yarn     yarn       235968 Dec 18 01:27 ./job.xml
 63318188      4 -rw-r--r--   1 yarn     yarn          129 Dec 18 01:27 ./container_tokens
 63318190      8 -rwx------   1 yarn     yarn         4932 Dec 18 01:27 ./launch_container.sh
 63318189      4 -rw-r--r--   1 yarn     yarn           12 Dec 18 01:27 ./.container_tokens.crc
 63318195      4 -rw-r--r--   1 yarn     yarn           16 Dec 18 01:27 ./.default_container_executor.sh.crc
broken symlinks(find -L . -maxdepth 5 -type l -ls):
""",
            "launch_container.sh": b"""#!/bin/bash

set -o pipefail -e
export PRELAUNCH_OUT="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/prelaunch.out"
exec >"${PRELAUNCH_OUT}"
export PRELAUNCH_ERR="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/prelaunch.err"
exec 2>"${PRELAUNCH_ERR}"
echo "Setting up env variables"
export JAVA_HOME=${JAVA_HOME:-"/opt/java/openjdk"}
export HADOOP_COMMON_HOME=${HADOOP_COMMON_HOME:-"/hadoop"}
export HADOOP_HDFS_HOME=${HADOOP_HDFS_HOME:-"/hadoop"}
export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/hadoop/etc/hadoop"}
export HADOOP_YARN_HOME=${HADOOP_YARN_HOME:-"/hadoop"}
export HADOOP_HOME=${HADOOP_HOME:-"/hadoop"}
export PATH=${PATH:-"/hadoop/bin:/hadoop/sbin:/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"}
export LANG=${LANG:-"en_US.UTF-8"}
export HADOOP_MAPRED_HOME=${HADOOP_MAPRED_HOME:-"/hadoop"}
export HADOOP_TOKEN_FILE_LOCATION="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000003/container_tokens"
export CONTAINER_ID="container_1671326373437_0001_01_000003"
export NM_PORT="36113"
export NM_HOST="hadoopnode"
export NM_HTTP_PORT="8042"
export LOCAL_DIRS="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001"
export LOCAL_USER_DIRS="/data/nm-local-dir/usercache/sandbox/"
export LOG_DIRS="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003"
export USER="sandbox"
export LOGNAME="sandbox"
export HOME="/home/"
export PWD="/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000003"
export LOCALIZATION_COUNTERS="0,518812,0,2,1"
export JVM_PID="$$"
export NM_AUX_SERVICE_mapreduce_shuffle="AAA0+gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
export STDOUT_LOGFILE_ENV="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/stdout"
export SHELL="/bin/bash"
export HADOOP_ROOT_LOGGER="INFO,console"
export CLASSPATH="$PWD:$HADOOP_CONF_DIR:$HADOOP_COMMON_HOME/share/hadoop/common/*:$HADOOP_COMMON_HOME/share/hadoop/common/lib/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/*:$HADOOP_HDFS_HOME/share/hadoop/hdfs/lib/*:$HADOOP_YARN_HOME/share/hadoop/yarn/*:$HADOOP_YARN_HOME/share/hadoop/yarn/lib/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*:job.jar/*:job.jar/classes/:job.jar/lib/*:$PWD/*"
export LD_LIBRARY_PATH="$PWD:$HADOOP_COMMON_HOME/lib/native"
export STDERR_LOGFILE_ENV="/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/stderr"
export HADOOP_CLIENT_OPTS=""
export MALLOC_ARENA_MAX="4"
echo "Setting up job resources"
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/11/job.jar" "job.jar"
ln -sf -- "/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/filecache/13/job.xml" "job.xml"
echo "Copying debugging information"
# Creating copy of launch script
cp "launch_container.sh" "/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/launch_container.sh"
chmod 640 "/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/launch_container.sh"
# Determining directory contents
echo "ls -l:" 1>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/directory.info"
ls -l 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/directory.info"
echo "find -L . -maxdepth 5 -ls:" 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/directory.info"
find -L . -maxdepth 5 -ls 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/directory.info"
echo "broken symlinks(find -L . -maxdepth 5 -type l -ls):" 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/directory.info"
find -L . -maxdepth 5 -type l -ls 1>>"/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/directory.info"
echo "Launching container"
exec /bin/bash -c "$JAVA_HOME/bin/java -Djava.net.preferIPv4Stack=true -Dhadoop.metrics.log.level=WARN   -Xmx820m -Djava.io.tmpdir=$PWD/tmp -Dlog4j.configuration=container-log4j.properties -Dyarn.app.container.log.dir=/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003 -Dyarn.app.container.log.filesize=0 -Dhadoop.root.logger=INFO,CLA -Dhadoop.root.logfile=syslog org.apache.hadoop.mapred.YarnChild 10.0.1.4 45261 attempt_1671326373437_0001_m_000001_0 3 1>/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/stdout 2>/hadoop/logs/userlogs/application_1671326373437_0001/container_1671326373437_0001_01_000003/stderr "
""",
            "prelaunch.err": b"""""",
            "prelaunch.out": b"""Setting up env variables
Setting up job resources
Copying debugging information
Launching container
""",
            "stderr": b"""""",
            "stdout": b"""""",
            "syslog": b"""2022-12-18 01:27:34,652 INFO [main] org.apache.hadoop.security.SecurityUtil: Updating Configuration
2022-12-18 01:27:34,705 INFO [main] org.apache.hadoop.metrics2.impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2022-12-18 01:27:34,749 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: Scheduled Metric snapshot period at 10 second(s).
2022-12-18 01:27:34,750 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MapTask metrics system started
2022-12-18 01:27:34,782 INFO [main] org.apache.hadoop.mapred.YarnChild: Executing with tokens: [Kind: mapreduce.job, Service: job_1671326373437_0001, Ident: (org.apache.hadoop.mapreduce.security.token.JobTokenIdentifier@1ebd319f)]
2022-12-18 01:27:34,807 INFO [main] org.apache.hadoop.mapred.YarnChild: Sleeping for 0ms before retrying again. Got null now.
2022-12-18 01:27:34,910 INFO [main] org.apache.hadoop.mapred.YarnChild: mapreduce.cluster.local.dir for child: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001
2022-12-18 01:27:35,049 INFO [main] org.apache.hadoop.mapred.YarnChild: 
/************************************************************
[system properties]
os.name: Linux
os.version: 6.0.0-6-amd64
java.home: /opt/java/openjdk/jre
java.runtime.version: 1.8.0_345-b01
java.vendor: Temurin
java.version: 1.8.0_345
java.vm.name: OpenJDK 64-Bit Server VM
java.class.path: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000003:/hadoop/etc/hadoop:/hadoop/share/hadoop/common/hadoop-nfs-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-kms-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-registry-3.3.4.jar:/hadoop/share/hadoop/common/hadoop-common-3.3.4-tests.jar:/hadoop/share/hadoop/common/hadoop-common-3.3.4.jar:/hadoop/share/hadoop/common/lib/kerby-pkix-1.0.1.jar:/hadoop/share/hadoop/common/lib/nimbus-jose-jwt-9.8.1.jar:/hadoop/share/hadoop/common/lib/jetty-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/asm-5.0.4.jar:/hadoop/share/hadoop/common/lib/paranamer-2.3.jar:/hadoop/share/hadoop/common/lib/commons-configuration2-2.1.1.jar:/hadoop/share/hadoop/common/lib/kerb-identity-1.0.1.jar:/hadoop/share/hadoop/common/lib/re2j-1.1.jar:/hadoop/share/hadoop/common/lib/jackson-xc-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-beanutils-1.9.4.jar:/hadoop/share/hadoop/common/lib/jsch-0.1.55.jar:/hadoop/share/hadoop/common/lib/commons-math3-3.1.1.jar:/hadoop/share/hadoop/common/lib/jackson-mapper-asl-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-security-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-codec-1.15.jar:/hadoop/share/hadoop/common/lib/gson-2.8.9.jar:/hadoop/share/hadoop/common/lib/j2objc-annotations-1.1.jar:/hadoop/share/hadoop/common/lib/jackson-core-asl-1.9.13.jar:/hadoop/share/hadoop/common/lib/jetty-webapp-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/animal-sniffer-annotations-1.17.jar:/hadoop/share/hadoop/common/lib/jackson-jaxrs-1.9.13.jar:/hadoop/share/hadoop/common/lib/kerby-util-1.0.1.jar:/hadoop/share/hadoop/common/lib/zookeeper-3.5.6.jar:/hadoop/share/hadoop/common/lib/accessors-smart-2.4.7.jar:/hadoop/share/hadoop/common/lib/reload4j-1.2.22.jar:/hadoop/share/hadoop/common/lib/jcip-annotations-1.0-1.jar:/hadoop/share/hadoop/common/lib/jersey-servlet-1.19.jar:/hadoop/share/hadoop/common/lib/metrics-core-3.2.4.jar:/hadoop/share/hadoop/common/lib/jersey-json-1.19.jar:/hadoop/share/hadoop/common/lib/jsp-api-2.1.jar:/hadoop/share/hadoop/common/lib/curator-client-4.2.0.jar:/hadoop/share/hadoop/common/lib/curator-recipes-4.2.0.jar:/hadoop/share/hadoop/common/lib/commons-text-1.4.jar:/hadoop/share/hadoop/common/lib/jersey-server-1.19.jar:/hadoop/share/hadoop/common/lib/kerb-simplekdc-1.0.1.jar:/hadoop/share/hadoop/common/lib/jersey-core-1.19.jar:/hadoop/share/hadoop/common/lib/avro-1.7.7.jar:/hadoop/share/hadoop/common/lib/commons-io-2.8.0.jar:/hadoop/share/hadoop/common/lib/kerb-core-1.0.1.jar:/hadoop/share/hadoop/common/lib/slf4j-api-1.7.36.jar:/hadoop/share/hadoop/common/lib/kerb-server-1.0.1.jar:/hadoop/share/hadoop/common/lib/commons-collections-3.2.2.jar:/hadoop/share/hadoop/common/lib/jackson-core-2.12.7.jar:/hadoop/share/hadoop/common/lib/commons-daemon-1.0.13.jar:/hadoop/share/hadoop/common/lib/snappy-java-1.1.8.2.jar:/hadoop/share/hadoop/common/lib/jettison-1.1.jar:/hadoop/share/hadoop/common/lib/kerb-common-1.0.1.jar:/hadoop/share/hadoop/common/lib/jetty-http-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/failureaccess-1.0.jar:/hadoop/share/hadoop/common/lib/jul-to-slf4j-1.7.36.jar:/hadoop/share/hadoop/common/lib/jaxb-api-2.2.11.jar:/hadoop/share/hadoop/common/lib/jsr311-api-1.1.1.jar:/hadoop/share/hadoop/common/lib/jaxb-impl-2.2.3-1.jar:/hadoop/share/hadoop/common/lib/javax.servlet-api-3.1.0.jar:/hadoop/share/hadoop/common/lib/zookeeper-jute-3.5.6.jar:/hadoop/share/hadoop/common/lib/jetty-util-ajax-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/commons-compress-1.21.jar:/hadoop/share/hadoop/common/lib/commons-net-3.6.jar:/hadoop/share/hadoop/common/lib/commons-cli-1.2.jar:/hadoop/share/hadoop/common/lib/checker-qual-2.5.2.jar:/hadoop/share/hadoop/common/lib/jetty-io-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/netty-3.10.6.Final.jar:/hadoop/share/hadoop/common/lib/kerb-crypto-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerby-asn1-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerby-xdr-1.0.1.jar:/hadoop/share/hadoop/common/lib/kerb-util-1.0.1.jar:/hadoop/share/hadoop/common/lib/commons-logging-1.1.3.jar:/hadoop/share/hadoop/common/lib/commons-lang3-3.12.0.jar:/hadoop/share/hadoop/common/lib/token-provider-1.0.1.jar:/hadoop/share/hadoop/common/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/hadoop/share/hadoop/common/lib/jakarta.activation-api-1.2.1.jar:/hadoop/share/hadoop/common/lib/httpclient-4.5.13.jar:/hadoop/share/hadoop/common/lib/hadoop-shaded-guava-1.1.1.jar:/hadoop/share/hadoop/common/lib/hadoop-annotations-3.3.4.jar:/hadoop/share/hadoop/common/lib/hadoop-auth-3.3.4.jar:/hadoop/share/hadoop/common/lib/jackson-databind-2.12.7.jar:/hadoop/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar:/hadoop/share/hadoop/common/lib/curator-framework-4.2.0.jar:/hadoop/share/hadoop/common/lib/woodstox-core-5.3.0.jar:/hadoop/share/hadoop/common/lib/audience-annotations-0.5.0.jar:/hadoop/share/hadoop/common/lib/kerb-client-1.0.1.jar:/hadoop/share/hadoop/common/lib/json-smart-2.4.7.jar:/hadoop/share/hadoop/common/lib/dnsjava-2.1.7.jar:/hadoop/share/hadoop/common/lib/jsr305-3.0.2.jar:/hadoop/share/hadoop/common/lib/kerb-admin-1.0.1.jar:/hadoop/share/hadoop/common/lib/httpcore-4.4.13.jar:/hadoop/share/hadoop/common/lib/protobuf-java-2.5.0.jar:/hadoop/share/hadoop/common/lib/kerby-config-1.0.1.jar:/hadoop/share/hadoop/common/lib/jetty-util-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/jackson-annotations-2.12.7.jar:/hadoop/share/hadoop/common/lib/jetty-xml-9.4.43.v20210629.jar:/hadoop/share/hadoop/common/lib/hadoop-shaded-protobuf_3_7-1.1.1.jar:/hadoop/share/hadoop/common/lib/stax2-api-4.2.1.jar:/hadoop/share/hadoop/common/lib/guava-27.0-jre.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-native-client-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-rbf-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-rbf-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-native-client-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-httpfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-client-3.3.4.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-client-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-3.3.4-tests.jar:/hadoop/share/hadoop/hdfs/hadoop-hdfs-nfs-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/kerby-pkix-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/nimbus-jose-jwt-9.8.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/asm-5.0.4.jar:/hadoop/share/hadoop/hdfs/lib/paranamer-2.3.jar:/hadoop/share/hadoop/hdfs/lib/commons-configuration2-2.1.1.jar:/hadoop/share/hadoop/hdfs/lib/kerb-identity-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/re2j-1.1.jar:/hadoop/share/hadoop/hdfs/lib/jackson-xc-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/jetty-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-beanutils-1.9.4.jar:/hadoop/share/hadoop/hdfs/lib/leveldbjni-all-1.8.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-dns-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-rxtx-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jsch-0.1.55.jar:/hadoop/share/hadoop/hdfs/lib/commons-math3-3.1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-http2-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-udt-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jackson-mapper-asl-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/okhttp-4.9.3.jar:/hadoop/share/hadoop/hdfs/lib/jetty-security-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/commons-codec-1.15.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-mqtt-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-native-macos-4.1.77.Final-osx-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/gson-2.8.9.jar:/hadoop/share/hadoop/hdfs/lib/j2objc-annotations-1.1.jar:/hadoop/share/hadoop/hdfs/lib/jackson-core-asl-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/jetty-webapp-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/animal-sniffer-annotations-1.17.jar:/hadoop/share/hadoop/hdfs/lib/okio-2.8.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-handler-proxy-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jackson-jaxrs-1.9.13.jar:/hadoop/share/hadoop/hdfs/lib/kerby-util-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/zookeeper-3.5.6.jar:/hadoop/share/hadoop/hdfs/lib/accessors-smart-2.4.7.jar:/hadoop/share/hadoop/hdfs/lib/reload4j-1.2.22.jar:/hadoop/share/hadoop/hdfs/lib/jcip-annotations-1.0-1.jar:/hadoop/share/hadoop/hdfs/lib/jersey-servlet-1.19.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-kqueue-4.1.77.Final-osx-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/jersey-json-1.19.jar:/hadoop/share/hadoop/hdfs/lib/curator-client-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/curator-recipes-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/commons-text-1.4.jar:/hadoop/share/hadoop/hdfs/lib/kotlin-stdlib-common-1.4.10.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-unix-common-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-all-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-epoll-4.1.77.Final-linux-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/jersey-server-1.19.jar:/hadoop/share/hadoop/hdfs/lib/netty-common-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-simplekdc-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jersey-core-1.19.jar:/hadoop/share/hadoop/hdfs/lib/avro-1.7.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-io-2.8.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-haproxy-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-core-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-sctp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-server-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/commons-collections-3.2.2.jar:/hadoop/share/hadoop/hdfs/lib/jackson-core-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-http-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-daemon-1.0.13.jar:/hadoop/share/hadoop/hdfs/lib/snappy-java-1.1.8.2.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-classes-epoll-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jettison-1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-smtp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-common-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-http-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/failureaccess-1.0.jar:/hadoop/share/hadoop/hdfs/lib/kotlin-stdlib-1.4.10.jar:/hadoop/share/hadoop/hdfs/lib/jaxb-api-2.2.11.jar:/hadoop/share/hadoop/hdfs/lib/netty-buffer-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-classes-macos-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jsr311-api-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/json-simple-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-stomp-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jaxb-impl-2.2.3-1.jar:/hadoop/share/hadoop/hdfs/lib/javax.servlet-api-3.1.0.jar:/hadoop/share/hadoop/hdfs/lib/zookeeper-jute-3.5.6.jar:/hadoop/share/hadoop/hdfs/lib/jetty-util-ajax-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-epoll-4.1.77.Final-linux-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/netty-handler-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-compress-1.21.jar:/hadoop/share/hadoop/hdfs/lib/commons-net-3.6.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-xml-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/commons-cli-1.2.jar:/hadoop/share/hadoop/hdfs/lib/checker-qual-2.5.2.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-native-kqueue-4.1.77.Final-osx-x86_64.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-memcache-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/jetty-io-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/netty-3.10.6.Final.jar:/hadoop/share/hadoop/hdfs/lib/kerb-crypto-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerby-asn1-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerby-xdr-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/kerb-util-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/commons-logging-1.1.3.jar:/hadoop/share/hadoop/hdfs/lib/commons-lang3-3.12.0.jar:/hadoop/share/hadoop/hdfs/lib/token-provider-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/hadoop/share/hadoop/hdfs/lib/jakarta.activation-api-1.2.1.jar:/hadoop/share/hadoop/hdfs/lib/httpclient-4.5.13.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-redis-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-shaded-guava-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-annotations-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-auth-3.3.4.jar:/hadoop/share/hadoop/hdfs/lib/jackson-databind-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/curator-framework-4.2.0.jar:/hadoop/share/hadoop/hdfs/lib/netty-resolver-dns-native-macos-4.1.77.Final-osx-aarch_64.jar:/hadoop/share/hadoop/hdfs/lib/woodstox-core-5.3.0.jar:/hadoop/share/hadoop/hdfs/lib/audience-annotations-0.5.0.jar:/hadoop/share/hadoop/hdfs/lib/kerb-client-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/json-smart-2.4.7.jar:/hadoop/share/hadoop/hdfs/lib/netty-codec-socks-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/netty-transport-classes-kqueue-4.1.77.Final.jar:/hadoop/share/hadoop/hdfs/lib/dnsjava-2.1.7.jar:/hadoop/share/hadoop/hdfs/lib/jsr305-3.0.2.jar:/hadoop/share/hadoop/hdfs/lib/kerb-admin-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/httpcore-4.4.13.jar:/hadoop/share/hadoop/hdfs/lib/protobuf-java-2.5.0.jar:/hadoop/share/hadoop/hdfs/lib/kerby-config-1.0.1.jar:/hadoop/share/hadoop/hdfs/lib/jetty-util-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/jackson-annotations-2.12.7.jar:/hadoop/share/hadoop/hdfs/lib/jetty-xml-9.4.43.v20210629.jar:/hadoop/share/hadoop/hdfs/lib/hadoop-shaded-protobuf_3_7-1.1.1.jar:/hadoop/share/hadoop/hdfs/lib/stax2-api-4.2.1.jar:/hadoop/share/hadoop/hdfs/lib/guava-27.0-jre.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-common-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-registry-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-router-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-client-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-distributedshell-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-services-core-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-nodemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-api-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-resourcemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-mawo-core-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-services-api-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-tests-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-applications-unmanaged-am-launcher-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-sharedcachemanager-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-web-proxy-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-timeline-pluginstorage-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-applicationhistoryservice-3.3.4.jar:/hadoop/share/hadoop/yarn/hadoop-yarn-server-common-3.3.4.jar:/hadoop/share/hadoop/yarn/lib/javax.websocket-api-1.0.jar:/hadoop/share/hadoop/yarn/lib/websocket-servlet-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/json-io-2.5.1.jar:/hadoop/share/hadoop/yarn/lib/jline-3.9.0.jar:/hadoop/share/hadoop/yarn/lib/bcprov-jdk15on-1.60.jar:/hadoop/share/hadoop/yarn/lib/websocket-common-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jetty-jndi-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/websocket-server-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jackson-module-jaxb-annotations-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/HikariCP-java7-2.4.12.jar:/hadoop/share/hadoop/yarn/lib/jersey-client-1.19.jar:/hadoop/share/hadoop/yarn/lib/metrics-core-3.2.4.jar:/hadoop/share/hadoop/yarn/lib/jetty-client-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/guice-servlet-4.0.jar:/hadoop/share/hadoop/yarn/lib/swagger-annotations-1.5.4.jar:/hadoop/share/hadoop/yarn/lib/bcpkix-jdk15on-1.60.jar:/hadoop/share/hadoop/yarn/lib/websocket-api-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jna-5.2.0.jar:/hadoop/share/hadoop/yarn/lib/jackson-jaxrs-base-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/javax-websocket-client-impl-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/snakeyaml-1.26.jar:/hadoop/share/hadoop/yarn/lib/asm-tree-9.1.jar:/hadoop/share/hadoop/yarn/lib/javax.websocket-client-api-1.0.jar:/hadoop/share/hadoop/yarn/lib/javax-websocket-server-impl-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jackson-jaxrs-json-provider-2.12.7.jar:/hadoop/share/hadoop/yarn/lib/asm-analysis-9.1.jar:/hadoop/share/hadoop/yarn/lib/websocket-client-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/ehcache-3.3.1.jar:/hadoop/share/hadoop/yarn/lib/guice-4.0.jar:/hadoop/share/hadoop/yarn/lib/fst-2.50.jar:/hadoop/share/hadoop/yarn/lib/jetty-plus-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/jetty-annotations-9.4.43.v20210629.jar:/hadoop/share/hadoop/yarn/lib/geronimo-jcache_1.0_spec-1.0-alpha-1.jar:/hadoop/share/hadoop/yarn/lib/mssql-jdbc-6.2.1.jre7.jar:/hadoop/share/hadoop/yarn/lib/objenesis-2.6.jar:/hadoop/share/hadoop/yarn/lib/jersey-guice-1.19.jar:/hadoop/share/hadoop/yarn/lib/jakarta.xml.bind-api-2.3.2.jar:/hadoop/share/hadoop/yarn/lib/aopalliance-1.0.jar:/hadoop/share/hadoop/yarn/lib/javax.inject-1.jar:/hadoop/share/hadoop/yarn/lib/asm-commons-9.1.jar:/hadoop/share/hadoop/yarn/lib/java-util-1.9.0.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-plugins-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-shuffle-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.4-tests.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-nativetask-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-app-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-uploader-3.3.4.jar:/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.3.4.jar:/hadoop/share/hadoop/mapreduce/lib/*:job.jar/job.jar:job.jar/classes/:job.jar/lib/*:/data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000003/job.jar
java.io.tmpdir: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000003/tmp
user.dir: /data/nm-local-dir/usercache/sandbox/appcache/application_1671326373437_0001/container_1671326373437_0001_01_000003
user.name: yarn
************************************************************/
2022-12-18 01:27:35,049 INFO [main] org.apache.hadoop.conf.Configuration.deprecation: session.id is deprecated. Instead, use dfs.metrics.session-id
2022-12-18 01:27:35,256 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: File Output Committer Algorithm version is 2
2022-12-18 01:27:35,256 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
2022-12-18 01:27:35,264 INFO [main] org.apache.hadoop.mapred.Task:  Using ResourceCalculatorProcessTree : [ ]
2022-12-18 01:27:35,338 INFO [main] org.apache.hadoop.mapred.MapTask: Processing split: org.apache.hadoop.examples.terasort.TeraGen$RangeInputFormat$RangeInputSplit@46f699d5
2022-12-18 01:27:35,684 INFO [main] org.apache.hadoop.mapred.Task: Task:attempt_1671326373437_0001_m_000001_0 is done. And is in the process of committing
2022-12-18 01:27:35,689 INFO [main] org.apache.hadoop.mapred.Task: Task attempt_1671326373437_0001_m_000001_0 is allowed to commit now
2022-12-18 01:27:35,697 INFO [main] org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter: Saved output of task 'attempt_1671326373437_0001_m_000001_0' to hdfs://namenode:8020/user/sandbox/teragen
2022-12-18 01:27:35,702 INFO [main] org.apache.hadoop.mapred.Task: Task 'attempt_1671326373437_0001_m_000001_0' done.
2022-12-18 01:27:35,706 INFO [main] org.apache.hadoop.mapred.Task: Final Counters for attempt_1671326373437_0001_m_000001_0: Counters: 27
	File System Counters
		FILE: Number of bytes read=0
		FILE: Number of bytes written=275762
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=85
		HDFS: Number of bytes written=50000000
		HDFS: Number of read operations=6
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Map-Reduce Framework
		Map input records=500000
		Map output records=500000
		Input split bytes=85
		Spilled Records=0
		Failed Shuffles=0
		Merged Map outputs=0
		GC time elapsed (ms)=33
		CPU time spent (ms)=1480
		Physical memory (bytes) snapshot=380235776
		Virtual memory (bytes) snapshot=2616180736
		Total committed heap usage (bytes)=606601216
		Peak Map Physical memory (bytes)=380235776
		Peak Map Virtual memory (bytes)=2616180736
	org.apache.hadoop.examples.terasort.TeraGen$Counters
		CHECKSUM=1074389572096518
	File Input Format Counters 
		Bytes Read=0
	File Output Format Counters 
		Bytes Written=50000000
2022-12-18 01:27:35,706 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: Stopping MapTask metrics system...
2022-12-18 01:27:35,707 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MapTask metrics system stopped.
2022-12-18 01:27:35,707 INFO [main] org.apache.hadoop.metrics2.impl.MetricsSystemImpl: MapTask metrics system shutdown complete.
""",
        },
    },
}


def test_splitter():
    with BytesIO(initial_bytes=INPUT_FIXTURE) as infile:
        with InMemoryOutputFolder() as of:
            split(infile=infile, output_folder=of)

    assert of.output == OUTPUT_FIXTURE
