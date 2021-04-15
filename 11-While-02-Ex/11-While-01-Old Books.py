book_name = input()
library_capacity = int(input())

book_counter = 0
new_book = ''

while new_book != book_name:
    if book_counter == library_capacity:
        print(f'The book you search is not here!')
        print(f'You checked {book_counter} books.')
        break
    book_counter += 1
    new_book = input()

if new_book == book_name:
    print(f'You checked {book_counter - 1} books and found it.')
