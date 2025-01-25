def main():
    BOOK_PATH = "./books/frankenstein.txt"
    with open(BOOK_PATH) as book:
        database = {}
        book_contents = book.read()
        for letter in book_contents:
            lower_letter = letter.lower()
            if lower_letter in database:
                database[lower_letter] += 1
            else:
                database[lower_letter] = 1
        print(database)
if __name__ == "__main__":
    main()

