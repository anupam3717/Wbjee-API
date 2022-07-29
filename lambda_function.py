import io
import csv
import boto3
import json


head=["general","pgeneral","obca","pobca","obcb","pobcb","sc","psc","st","pst","tfw"]
s3 = boto3.client('s3')
obj = s3.get_object(Bucket = 'testcsvforapi', Key = 'bbb.csv')
lines = obj['Body'].read().decode("utf-8")

def lambda_handler(event, context):
    a={}
    gmr=int(event["queryStringParameters"]["rank"])
    category=int(event["queryStringParameters"]["quota"])
    buf = io.StringIO(lines)
    reader = csv.DictReader(buf)
    for row in reader:
        if gmr<int(row[head[category]]):
            if row["quota"]=="HS":
                if a.get(row["college"])==None:
                    a[row["college"]]=[row["branch"]]
                else:
                    a[row["college"]].append(row["branch"])
    print(json.dumps(a,indent = 6))
    return {
        "statusCode": 200,
        "body": json.dumps(a,indent = 6)
    }