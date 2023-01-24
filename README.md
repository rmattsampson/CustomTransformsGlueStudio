# CustomTransformsGlueStudio
This repository contains Custom Transforms Samples for AWS Glue Studio

You can learn more about Custom Glue Visual Transforms here: https://docs.aws.amazon.com/glue/latest/ug/custom-visual-transform.html 

Upload the two files (Python source file and JSON config file) to the Amazon S3 assets folder where the job scripts are stored. By default, AWS Glue pulls all JSON files from the /transforms folder within the same Amazon S3 bucket.
They will then display in your Actions drop down in Glue Studio.  

List of Transforms:
1) CustomTransform_FillEmptyStringsInAColumn -> This transform allows you to select a Column you want to fill all the Null Values
