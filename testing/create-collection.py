from ..aws.rekognition.collection import create_collection

if __name__ == '__main__':
    collection_id = 'My-Collection'
    create_collection(collection_id)
