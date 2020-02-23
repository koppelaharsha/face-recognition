from ..aws.rekognition.faces import search_face

if __name__ == '__main__':
    image_path = '../../images/img-8.jpg'
    collectionId = 'My-Collection'
    search_face(image_path, collectionId)
    