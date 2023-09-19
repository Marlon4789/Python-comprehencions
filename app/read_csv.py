import csv # para leer un archivo  csv.

def read_cvs(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        for row in reader:
            print('***' * 3)
            print(row)

if __name__ == '__main__':
    read_cvs('./app/database.csv')
