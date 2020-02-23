from ..aws.dynamoDB.items import get_item

if __name__ == '__main__':
    table_name = 'Faces'
    item_key = {
        'face-id' : 'FACE-ID'
    }
    print(get_item(table_name, item_key))

