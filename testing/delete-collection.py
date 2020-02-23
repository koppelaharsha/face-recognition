from ..aws.rekognition.collection import delete_collection

if __name__ == '__main__':
    collection_id = 'My-Collection'
    delete_collection(collection_id)
