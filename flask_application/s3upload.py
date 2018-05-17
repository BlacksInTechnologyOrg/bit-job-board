import os
import boto3
from flask_application.awskey import bucket
from flask_application.users.models import User
from flask_login import current_user

def uploadprofilepic(file, user,acl="public-read"):

    file.filename = current_user.username + "_profilepic_" + ".jpg"
    try:
        s3 = boto3.client('s3')
        s3.put_object(
            Bucket=bucket,
            Body=file,
            ContentType=file.content_type,
            ACL=acl,
            Key="Profiledata/"+ user + "/images/profiledata/" + file.filename,
            Tagging="profilepic"
        )
        # s3.upload_fileobj(file,
        #                   bucket,
        #                   "Profiledata/"+ user + "/images/profiledata/" + file.filename,
        #                   ExtraArgs={
        #                       "ACL": acl,
        #                       "ContentType": file.content_type,
        #                       "Tagging":"profilepic"
        #                   }
        # )
    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e