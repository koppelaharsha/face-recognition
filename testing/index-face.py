from ..aws.rekognition.faces import index_face

if __name__ == '__main__':
    collection_id = 'My-Collection'
    image_path = '../images/img-7.jpg'
    index_face(collection_id, image_path)
