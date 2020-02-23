import boto3

def create_table(table):
    dynamodb = boto3.client('dynamodb')
    try:
        print('Creating Table')
        response = dynamodb.create_table(
            TableName = table['Name'],
            KeySchema = table['KeySchema'],
            AttributeDefinitions = table['Attributes'],
            ProvisionedThroughput = table['ProvisionedThroughput']
            )
        print('Done...')
    except:
        print('Error Creating Table')

def delete_table(table_name):
    dynamodb = boto3.client('dynamodb')
    try:
        print('Deleting Table')
        response = dynamodb.delete_table(
            TableName = table_name
            )
        print('Done...')
    except:
        print('Error Deleting Table')
