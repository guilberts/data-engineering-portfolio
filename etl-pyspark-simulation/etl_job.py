from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, when


# Set the path to writing parquet
destination_path = 'output_movies'

# intializing Spark session (simulating Job)
spark = SparkSession.builder \
    .appName("ETL_PySpark_Simulation") \
    .getOrCreate()

# 1. reading CSV data source (raw data)
df = spark.read.csv("data/source/movies.csv", header=True, inferSchema=True)

print("=== Raw Data ===")
df.show(5, truncate=False)
print(f"Total records: {df.count()}")

# 2. Transformation: filtering movies and selecting columns
df_transformed = df.filter(year(col("release_date")) > 2000) \
                   .select("movie_id", "title", "release_date", "vote_average")

print("\n=== Filtering Data (over 2000) ===")
df_transformed.show(5, truncate=False)
print(f"Filtered total records: {df_transformed.count()}")

# 3. Enritchment: creating new classified column
df_final = df_transformed.withColumn(
        "rating_category",
        when(col("vote_average") < 5, "Poor")
        .when(col("vote_average") < 7, "Average")
        .when(col("vote_average") < 8, "Good")
        .otherwise("Excellent")
)

print("\n=== Show Classified Data ===")
df_final.show(10, truncate=False)

# Show infered schema
print("\n=== Final Schema ===")
df_final.printSchema()

# 4. Write parquet output (Simulating Job)
df_final.write.mode("overwrite").parquet(destination_path)

print(f"\n✓ Data recorded at: {destination_path}")

spark.stop()