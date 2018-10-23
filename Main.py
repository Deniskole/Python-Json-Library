import json
import sys

from Book import *

"""Denys Kolesnikov"""
"""Variant 9 """

books = []
flag = True


# MAIN LOOP
def begin():
    print('---------------------- Books ----------------------')
    print('Add book = a')
    print('Show books = s')
    print('Exit = e')
    print('----------------- Make your choice ----------------')


begin()


# INTO DICTIONARY FOR DUMP JSON LIB
def inDictionary(book):
    bookDictionary = {'name': book.name,
                      'number_of_authors': book.number_of_authors,
                      'authors': book.authors,
                      'year_of_publishing': book.year_of_publishing,
                      'number_of_pages': book.number_of_pages
                      }
    return bookDictionary


# LOAD JSON FILE
def get_json_data():
    try:
        fileread = open('booksJson.txt', 'r', encoding='Latin-1')
        json_data = json.load(fileread)
        fileread.close()
        return json_data
    except Exception:
        print('File is empty....')
        print(sys.exc_info()[1])
        return False


# GET ARRAY EXIST BOOKS
def get_json_exist_books():
    exist_books = []
    for book1 in get_json_data():
        book3 = Book(book1['name'], book1['number_of_authors'], book1['authors'], book1['year_of_publishing'],
                     book1['number_of_pages'])
        exist_books.append(inDictionary(book3))
    return exist_books

while flag:

    choice = str(input())

    if choice == 'a':
        authors_array = []
        authors_array.clear()

        print('ADD BOOK')
        name = input('STEP 1.Book name: ')
        number_of_authors = input('STEP 2.Amount authors: ')

        for x in range(0, int(number_of_authors)):
            name_authors = input('STEP 3.Author #' + str(x + 1) + ': ')
            authors_array.append(name_authors)

        year_of_publishing = input('4.Year of publishing: ')
        number_of_pages = input('5.Number of pages: ')

        # Add to JSON-------------------

        data = []
        book = Book(name, number_of_authors, authors_array, year_of_publishing, number_of_pages)

        for y in get_json_exist_books():
            data.append(y)

        data.append(inDictionary(book))

        fileopen = open('booksJson.txt', 'w')
        json.dump(data, fileopen)

        fileopen.close()
        data.clear()

        print('\n-----The book was added successfully-----\n')
        book.show_book()
        books.append(book)
        print(' ')

        begin()

    elif choice == 's':
        print('SHOW HERE')

        # Read JSON File
        counterBook = 1
        print('--------------------READ JSON FILE!--------------------')
        for book in get_json_data():
            print('\n--- Book #' + str(counterBook) + ' ---')
            counterBook = counterBook + 1
            print('Name: ' + str(book['name']))
            print('Amount authors: ' + str(book['number_of_authors']))

            counter = 1
            arrays = list(book['authors'])
            for author in arrays:
                print('Author #' + str(counter) + ': ' + author)
                counter = counter + 1

            print('Year of publishing: ' + str(book['year_of_publishing']))
            print('Amount Pages: ' + str(book['number_of_pages']))

    elif choice == 'e':
        print('Close programm!')
        flag = False
    else:
        print('Type Wrong!')
