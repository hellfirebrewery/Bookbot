def main():
    filename = "books/frankenstein.txt"
    output = get_book_text(filename)
    from stats import word_count
    count = word_count(output)
    print(f"{count} words found in the document")

def get_book_text(filename):
    with open(filename) as f:
    # do something with f (the file) here
   
    # f is a file object
        return f.read()


main()
