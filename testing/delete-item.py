from ..aws.dynamoDB.items import delete_item

if __name__ == '__main__':
    table_name = 'Faces'
    item_key = {
        'face-id' : 'FACE-ID'
    }
    delete_item(table_name, item_key)
