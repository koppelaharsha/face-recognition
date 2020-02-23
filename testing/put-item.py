from ..aws.dynamoDB.items import put_item

if __name__ == '__main__':
    table_name = 'Faces'
    item = {
        'face-id' : 'FACE-ID',
        'person-id' : 'NAME'
    }
    put_item(table_name, item)
