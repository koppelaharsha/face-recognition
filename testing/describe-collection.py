from ..aws.rekognition.collection import describe_collection

if __name__ == '__main__':
    collection_id = 'My-Collection'
    describe_collection(collection_id)
