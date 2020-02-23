import boto3

def create_collection(collection_id):
    client = boto3.client('rekognition')
    try:
        print('creating collection: ' + collection_id)
        response = client.create_collection(CollectionId=collection_id)
        print('Collection ARN: ' + response['CollectionArn'])
        print('Done...')
    except:
        print('Error Creating Collection')

def describe_collection(collection_id):
    client = boto3.client('rekognition')
    try:
        print('Describing Collection: ' + collection_id)
        response = client.describe_collection(CollectionId=collection_id)
        print('Collecion ARN: ' + response['CollectionARN'])
        print('Face Count: ' + str(response['FaceCount']))
        print('Face Model Version: ' + response['FaceModelVersion'])
        print('Timestamp: ' + str(response['CreationTimestamp']))
        print('Done...')
    except:
        print('Error Describing Collection')

def list_collections():
    client = boto3.client('rekognition')
    try:
        max_results = 2
        print('Listing Collections')
        response = client.list_collections(MaxResults=max_results)
        collections_list = []
        done = False
        print('Displaying Collections')
        while done==False:
            collections = response['CollectionIds']
            for collection in collections:
                collections_list.append(collection)
            if 'NextToken' in response:
                nextToken = response['NextToken']
                response = client.list_collections(NextToken=nextToken,MaxResults=max_results)
            else:
                done = True
        print('Done...')
        return collections_list
    except:
        print('Error Listing Collections')

def delete_collection(collection_id):
    client = boto3.client('rekognition')
    try:
        print('Deleting Collection: ' + collection_id)
        response = client.delete_collection(CollectionId=collection_id)
        print('Done...')
    except:
        print('Error Deleting Collection')
