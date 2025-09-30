import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import year, col

@pytest.fixture(scope="session")
def spark():
    """
    Create a SparkSession for testing with single-threaded local mode.
    Yields the session and ensures proper cleanup after all tests complete.
    """
    spark = SparkSession.builder \
        .appName("PySparkETLTest") \
        .master("local[1]") \
        .getOrCreate()
    yield spark
    spark.stop()


def test_etl_transformation(spark):
    """
    Test ETL transformation pipeline including filtering, selection, and rating categorization.
    
    Validates:
    - Movies filtered by release year (>2000)
    - Rating category column creation
    - Correct category assignment based on vote average
    """
    # Arrange: Create sample input data
    data = [
        (1, "Movie A", "1999-05-01", 6.5),
        (2, "Movie B", "2005-07-15", 8.1),
        (3, "Movie C", "2010-11-20", 4.3),
    ]
    columns = ["movie_id", "title", "release_date", "vote_average"]

    df = spark.createDataFrame(data, columns)

    # Act: Apply transformation - filter by year and select relevant columns
    df_transformed = df.filter(year(col("release_date")) > 2000) \
                       .select("movie_id", "title", "release_date", "vote_average")

    # Act: Apply rating categorization logic
    from pyspark.sql.functions import when
    df_final = df_transformed.withColumn(
        "rating_category",
        when(col("vote_average") < 5, "Poor")
        .when(col("vote_average") < 7, "Average")
        .when(col("vote_average") < 8, "Good")
        .otherwise("Excellent")
    )

    # Assert: Verify only movies released after 2000 are present
    years = [int(r.release_date.split("-")[0]) for r in df_final.collect()]
    assert all(y > 2000 for y in years), "All movies should be released after 2000"

    # Assert: Verify rating_category column exists in output schema
    assert "rating_category" in df_final.columns, "rating_category column should exist"

    # Assert: Verify correct rating categorization for a specific record
    row_b = df_final.filter(col("title") == "Movie B").collect()[0]
    assert row_b.rating_category == "Excellent", "Movie B with rating 8.1 should be categorized as Excellent"