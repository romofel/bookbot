def main():
    BOOK_PATH = "./books/frankenstein.txt"
    with open(BOOK_PATH) as book:
        database = {}
        book_contents = book.read()
        words = book_contents.split()
        print(len(words))

if __name__ == "__main__":
    main()

