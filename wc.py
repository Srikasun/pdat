hdfs dfs -mkdir /mydata
echo "hello world hello hadoop mapreduce world" > sample.txt
hdfs dfs -put sample.txt /mydata
  mapper.py   #!/usr/bin/env python3
import sys

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        print(f"{word}\t1")
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        print(f"{word}\t1")
reducer.py
#!/usr/bin/env python3
import sys

current_word = None
count = 0

for line in sys.stdin:
    word, value = line.strip().split("\t")
    value = int(value)

    if current_word == word:
        count += value
    else:
        if current_word:
            print(f"{current_word}\t{count}")
        current_word = word
        count = value

# print last word
if current_word:
    print(f"{current_word}\t{count}")

chmod +x mapper.py reducer.py
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -input /mydata/sample.txt \
    -output /mydata/output_wordcount \
    -mapper mapper.py \
    -reducer reducer.py
hdfs dfs -cat /mydata/output_wordcount/part-00000

