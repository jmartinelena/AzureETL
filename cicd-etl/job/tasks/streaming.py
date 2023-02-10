from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from session.logger import Log4j

def main(spark,patterns):
    '''
    Main Streming Script.
        Input : param spark :> Spark instancia.
        Output: return      :> None.
    '''
    for Iter in patterns:
        match Iter:                                      
            case "VentasInternet.csv":  
                                    
                def tail(filePathsInput, n=10):
                      'Return the last n lines of a file'
                    with open(filePathsInput) as f:
                        return deque(f, n)
                 
                if len(sys.argv) == 0:
                    # Blobs storage
                    filePaths = "wasbs://" + blob_container \
                                             + "@" + storage_name \
                                             + f".blob.core.windows.net/{Iter}"
                else:
                    # Local
                    filePths = f'file:/opt/spark/spark-warehouse/{Iter}'
                    # Hadoop nodo
                    filePathsInput = f'hdfs://127.0.0.1:9000/user/fede/input/{Iter}' 
                    filePathsOutput = f'hdfs://127.0.0.1:9000/user/fede/output/{Iter}' 
                    
                    # Spark DataFrame Infiriendo el esquema y especificando que el archivo contiene encavezado,
                                        
                    socketDF.isStreaming()    # Returns True for DataFrames that have streaming sources
                    raw_df = spark.readStream \
                                    .format("csv") \
                                    .option("path", filePathsInput) \
                                    .option("maxFilesPerTrigger", 1) \
                                    .load()

                    explode_df = raw_df.selectExpr("InvoiceNumber", "CreatedTime", "StoreID", "PosID",
                                   "CustomerType", "PaymentMethod", "DeliveryType", "DeliveryAddress.City",
                                   "DeliveryAddress.State",
                                   "DeliveryAddress.PinCode", "explode(InvoiceLineItems) as LineItem")

                    flattened_df = explode_df \
                        .withColumn("ItemCode", expr("LineItem.ItemCode")) \
                        .withColumn("ItemDescription", expr("LineItem.ItemDescription")) \
                        .withColumn("ItemPrice", expr("LineItem.ItemPrice")) \
                        .withColumn("ItemQty", expr("LineItem.ItemQty")) \
                        .withColumn("TotalValue", expr("LineItem.TotalValue")) \
                        .drop("LineItem")

                    invoiceWriterQuery = flattened_df.writeStream \
                        .format("csv") \
                        .queryName("Flattened Invoice Writer") \
                        .outputMode("append") \
                        .option("path", filePathsOutput) \
                        .option("checkpointLocation", "chk-point-dir") \
                        .trigger(processingTime="1 minute") \
                        .start()

                    socketDF.printSchema()

                    # Read all the csv files written atomically in a directory
                    userSchema = StructType().add("name", "string").add("age", "integer")

                    csvDF = spark \
                            .readStream \
                            .option("sep", ";") \
                            .schema(userSchema) \
                            .csv(filePths)  # Equivalent to format("csv").load("/path/to/directory")
                                    
                    logger.info("Flattened Invoice Writer started")
                    invoiceWriterQuery.awaitTermination()
                continue    

            case _:
                raise ValueError("No se encuenta el Arcvhivo.")
    return None

if __name__ == "__main__":
     
    import dotenv
    import sys
    import os
    spark = SparkSession \
            .builder \
            .appName("File Streaming Demo") \
            .master("local[3]") \
            .config("spark.streaming.stopGracefullyOnShutdown", "true") \
            .config("spark.sql.streaming.schemaInference", "true") \
            .getOrCreate()

    logger = Log4j(spark)
    main(spark,patterns)
