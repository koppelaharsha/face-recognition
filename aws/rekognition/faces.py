import boto3

def index_face(collection_id, image_path):
    client = boto3.client('rekognition')
    try:
        print('Reading Image')
        with open(image_path, 'rb') as image:
            print('Indexing Face')
            response = client.index_faces(
                CollectionId = collection_id,
                Image = {'Bytes':image.read()}
                )
            print(response)
            print('Done...')
            return response['FaceRecords'][0]['Face']['FaceId']
    except:
        print('Error Indexing Image')

def list_faces(collection_id):
    client = boto3.client('rekognition')
    try:
        print('Listing Faces')
        max_results = 2
        response = client.list_faces(
            CollectionId = collection_id,
            MaxResults = max_results
            )
        tokens = True
        faces_count = 0
        face_ids = []
        while tokens:
            faces = response['Faces']
            for face in faces:
                face_ids.append(face['FaceId'])
                faces_count+=1
            if 'NextToken' in response:
                nextToken = response['NextToken']
                response = client.list_faces(
                    CollectionId = collection_id,
                    NextToken = nextToken,
                    MaxResults = max_results
                    )
            else:
                tokens = False
        print('Total faces = ' + str(faces_count))
        print('Done...')
        return face_ids
    except:
        print('Error Listing Faces')

def search_face(collection_id, image_path):
    client = boto3.client('rekognition')
    try:
        print('Reading Image')
        with open(image_path, 'rb') as image:
            print('Searching Face')
            response = client.search_faces_by_image(
                CollectionId = collection_id,
                Image = {'Bytes' : image.read()},
                FaceMatchThreshold = 90,
                MaxFaces = 1
                )
            faceMatches = response['FaceMatches']
            if len(faceMatches)==0:
                return 'No Match Found'
            else:
                matches = []
                for faceMatch in faceMatches:
                    match = {
                        'Id' : faceMatch['Face']['FaceId'],
                        # 'Box' : faceMatch['Face']['BoundingBox'],
                        'Similarity' : "{:.2f}".format(faceMatch['Similarity']) + "%"
                    }
                    matches.append(match)
                print('Done...')
                return matches[0]
    except:
        print('Error Searching Face')
        return 'No Match Found'

def delete_faces(collection_id, faces):
    client = boto3.client('rekognition')
    try:
        print('Deleting faces')
        response = client.delete_faces(
            CollectionId = collection_id,
            FaceIds = faces
            )
        print(str(len(response['DeletedFaces'])) + ' faces deleted')
        for faceId in response['DeletedFaces']:
            print(faceId)
        print('Done...')
    except:
        print('Error Deleting Face')
