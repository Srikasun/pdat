sudo apt update
sudo apt install openjdk-11-jdk -y
java -version
pip install pyspark
python -c "import pyspark; print(pyspark.__version__)"
pip install notebook
jupyter notebook
from pyspark.sql import SparkSession
| customerID | age | salary | tenure | num_products | Churn |
| ---------- | --- | ------ | ------ | ------------ | ----- |
| C001       | 35  | 50000  | 5      | 2            | No    |
| C002       | 42  | 60000  | 2      | 3            | Yes   |
| C003       | 29  | 45000  | 3      | 1            | No    |
# Step 1: Import Libraries
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Step 2: Initialize Spark Session
spark = SparkSession.builder \
    .appName("Customer Churn Prediction") \
    .getOrCreate()

# Step 3: Load Dataset
data = spark.read.csv("customer_churn.csv", header=True, inferSchema=True)
print("=== Sample Data ===")
data.show(5)

# Step 4: Preprocess Data
# Convert target categorical column 'Churn' to numeric
indexer = StringIndexer(inputCol="Churn", outputCol="label")
data = indexer.fit(data).transform(data)

# Combine feature columns into a single vector
feature_cols = ["age", "salary", "tenure", "num_products"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
data = assembler.transform(data)

print("=== Processed Data ===")
data.select("features", "label").show(5)

# Step 5: Split Data into Train and Test Sets
train_data, test_data = data.randomSplit([0.7, 0.3], seed=42)

# Step 6: Train Logistic Regression Model
lr = LogisticRegression(featuresCol="features", labelCol="label")
model = lr.fit(train_data)

# Step 7: Make Predictions
predictions = model.transform(test_data)
predictions.select("features", "label", "prediction", "probability").show(10)

# Step 8: Evaluate Model Accuracy
evaluator = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="accuracy"
)
accuracy = evaluator.evaluate(predictions)
print(f"Model Accuracy: {accuracy*100:.2f}%")

# Stop Spark Session
spark.stop()
python churn_prediction.py
