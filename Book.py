class Book:
    def __init__(self, name, number_of_authors, authors, year_of_publishing, number_of_pages):
        self.name = name
        self.number_of_authors = str(number_of_authors)
        self.authors = authors
        self.year_of_publishing = str(year_of_publishing)
        self.number_of_pages = str(number_of_pages)

    def add_author(self):
        print('Read book: ' + self.name)

    def what_year_of_book(self):
        print('Year of book: ' + str(self.year))

    def who_author_of_book(self):
        print('Authot of book: ' + self.author)

    def show_book(self):
        counter = 1
        print('Book: ' + self.name)
        print('Number of authors: ' + self.number_of_authors)

        for author in self.authors:
            print('Author #' + str(counter) + ': ' + author)
            counter = counter + 1

        print('Year of publishing:  ' + self.year_of_publishing)
        print('Number of pages: ' + self.number_of_pages)
