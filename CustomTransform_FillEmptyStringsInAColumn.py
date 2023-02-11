import pyspark.sql.functions as F
from awsglue import DynamicFrame
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.types import StructType
from pyspark.context import SparkContext
from pyspark.sql.functions import col,isnan, when, count, regexp_replace
#from typing import Union

def fill_null_values_txn(self, columnName, newValue):
        gluectx = self.glue_ctx
        _df = self.toDF()
        modifiedDF = _df.withColumn(columnName,when(col(columnName)=="" , newValue).otherwise(col(columnName)))
        _dyf = DynamicFrame.fromDF(modifiedDF, self.glue_ctx, self.name)
        return _dyf

DynamicFrame.fill_null_values_txn = fill_null_values_txn
