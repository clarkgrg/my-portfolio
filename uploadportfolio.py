import io
import boto3
import zipfile
import mimetypes

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:988518307686:displayPortfolioTopic')

    try:
        s3 = boto3.resource('s3')

        build_bucket = s3.Bucket('portfoliobuild.excelapis.com')
        portfolio_zip = io.BytesIO()
        build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)
        portfolio_bucket = s3.Bucket('portfolio.excelapis.com')

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj,nm,
                    ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
        print("Job Done")
        topic.publish(Subject='Portfolio Deployed', Message='Portfolio Deployed Successfully')
    except:
        topic.publish(Subject='Portfolio Deploy Failed', Message='Portfolio NOT Deployed Successfully')
        raise

    return 'Hello from Lambda'
