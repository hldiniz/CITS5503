from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def index(request):
        template = loader.get_template('files.html')
        dynamodb = boto3.resource(
                'dynamodb', region_name='ap-southeast-2',
                )

        table = dynamodb.Table('22600608-files')
        items = []
        try:
                response = table.scan()
        except ClientError as e:
                print(e.response['Error']['Message'])
        else:
                context = {'items': response['Items'] }
                return HttpResponse(template.render(context, request))
