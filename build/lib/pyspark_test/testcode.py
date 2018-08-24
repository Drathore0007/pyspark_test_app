from pyspark.sql import functions as f
    
def with_life_goal(df):
    return df.withColumn("life_goal", f.lit("escape!"))
