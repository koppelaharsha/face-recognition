from ..aws.dynamoDB.table import delete_table

if __name__ == '__main__':
    table_name = 'Faces'
    delete_table(table_name)
