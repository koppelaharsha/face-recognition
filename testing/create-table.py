from ..aws.dynamoDB.table import create_table

if __name__ == '__main__':
    table = {
        'Name' : 'Faces',
        'KeySchema' : [
            {
                'AttributeName' : 'face-id',
                'KeyType' : 'HASH'
            }
        ],
        'Attributes' : [
            {
                'AttributeName' : 'person-id',
                'AttributeType' : 'S'
            }
        ],
        'ProvisionedThroughput' : {
            'ReadCapacityUnits' : 10,
            'WriteCapacityUnits' : 10
        }
    }
    create_table(table)
