from ..aws.rekognition.faces import search_face

if __name__ == '__main__':
    collection_id = 'My-Collection'
    image_path = '../images/img-8.jpg'
    search_face(collection_id, image_path)
