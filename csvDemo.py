import sys
import os
import csv
import re



def separarTelefonos():
    telefonos = [
        "2121-4735/4212-2545",
        "4775-4735 / 5218-2145",
        "4764-4738 / 5229-2545/15-4514-5944",
        "4780-6516 15-6869-2197"
    ]

    for phone in telefonos:
        result = phone.split('/')
        if len(result) == 1:
            result = phone.split(' ')

        result1 = []
        for newPhone in result:
            result1.append(newPhone.replace('-', ''))

        print("Telefono: ", phone, " Result: ", result1)


def readCSV():
    # loads JSON from a file.
    txtFile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'cliente.txt'))

    with open(txtFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\tCliente: {row[1]} Nombre {row[2]} Telefono {row[7]}.')
                line_count += 1

    print(f'Processed {line_count} lines.')


def main(argv):
    # readCSV()

    separarTelefonos()


def init():
    if __name__ == '__main__':
        sys.exit(main(sys.argv))

init()
