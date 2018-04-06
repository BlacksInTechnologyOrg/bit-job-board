import os
import boto3
from flask_application.awskey import bucket
from flask_login import current_user

def uploadprofilepic(file, user,acl="public-read"):

    file.filename = current_user.username + "_profilepic.jpg"
    print(file.filename)
    try:
        s3 = boto3.client('s3')
        s3.upload_fileobj(file,
                          bucket,
                          user + "/images/profiledata/" + file.filename,
                          ExtraArgs={
                              "ACL": acl,
                              "ContentType": file.content_type
                          }
        )
    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e