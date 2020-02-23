from ..aws.rekognition.faces import delete_faces

if __name__ == '__main__':
    collection_id = 'My-Collection'
    faces = ['FACE-ID']
    delete_faces(collection_id, faces)
