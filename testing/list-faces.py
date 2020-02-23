from ..aws.rekognition.faces import list_faces

if __name__ == '__main__':
    collection_id = 'My-Collection'
    list_faces(collection_id)
