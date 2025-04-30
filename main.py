def get_book_text(filename):
    with open(filename) as f:
    # do something with f (the file) here
   
   # f is a file object
        file_contents = f.read()
    return file_contents


def main():
    filename = "books/frankenstein.txt"
    output = get_book_text(filename)
    print(output)

main()
