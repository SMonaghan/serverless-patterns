from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job


sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

input_loc = "s3://my-glue-job-bucket/glue-python-assets/file.csv"
output_loc = "s3://my-glue-job-bucket/glue-python-assets/"

inputDyf = glueContext.create_dynamic_frame_from_options(
    connection_type="s3",
    connection_options={
        "paths": [input_loc]
    },
    format="csv",
    format_options={
        "withHeader": True,
        "separator": ","
    })


outputDF = glueContext.write_dynamic_frame.from_options(
    frame=inputDyf,
    connection_type="s3",
    connection_options={"path": output_loc
        },
    format="parquet")

