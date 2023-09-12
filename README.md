# 👋 The 100 latest repositories for technology company (Apple, Google, Microsoft, Netflix, Meta)

The repository is dedicated for the depolyment of function in AWS Lambda. Before deploying the function, make sure to have a valid AWS account with proper IAM role configuration. You may check out the visualisation and blog post on links below:

- Medium Blog Post: https://medium.com/@kangzhiyong1999/is-my-first-data-science-portfolio-using-aws-services-considered-a-data-engineerinng-project-b7f721bdba82
- Tableu Public: https://public.tableau.com/app/profile/kang.zhi.yong/viz/Top-100-Repos-Tech-Company/Dashboard1

## 👀 About the function 

The function is available under the directory "zipfiles/github-faang-lambda.zip". To test this function, you may directly upload this zipfile to AWS Lambda Console and set some of the environment variables as below:

- BOOKMARK_FILE	: bookmark
- BOOKMARK_NAME	: bookmark_details.json
- BUCKET_NAME   : "Your S3 bucket name"
- ENVIRON	      : DEV
- token	        : "Your Github API token"

To just view the function, you may refer to the python file called lambda function.py and edit accordingly for your need. The packages is with the additional python packages that not available in AWS Lambda. In our case, the packages directory is with the requests modules

You may zip the modules in packages directory and all the neccessary python file before uploading to AWS Lambda console after ammendment using commands as below:

```
# change to the directory with external modules
cd /path/to/packages

# zip the file in the directory
zip -r ../github-faang-lambda .

# back one directory
cd ..

# zip the packages with python files
zip github-faang-lambda.zip *py 

```
## 👀 What data is being requested?

The 100 latest repositories of the company is requested using Github API and details can be found in the download.py file 

## 👀 What is the use of Notebook?

The jupyter notebook named "Validation-lambda.ipynb" is used to validate the lambda function in lambda_function.py. Meanwhile, the "Extract_data_from_s3" is used to request the latest data from S3 bucket and proccessed before loading to the Tableau Pulic for visualisation. 




