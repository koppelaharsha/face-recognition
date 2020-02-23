import boto3

def put_item(table_name, item):
    dynamodb = boto3.resource('dynamodb')
    try:
        print('Adding Item')
        table = dynamodb.Table(table_name)
        table.put_item(Item = item)
        print('Done...')
    except:
        print('Error Adding Item')

def get_item(table_name, item_key):
    dynamodb = boto3.resource('dynamodb')
    try:
        print('Retrieving Item')
        table = dynamodb.Table(table_name)
        response = table.get_item(Key = item_key)
        print('Done...')
        return response['Item']['person-id']
    except:
        print('Error Retrieving Item')
        return 'No Name Found'

def delete_item(table_name, item_key):
    dynamodb = boto3.resource('dynamodb')
    try:
        print('Deleting Item')
        table = dynamodb.Table(table_name)
        table.delete_item(Key = item_key)
        print('Done...')
    except:
        print('Error Deleting Item')
