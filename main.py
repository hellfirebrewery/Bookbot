def get_book_text(filename):
    with open(filename) as f:
     #do something with f (the file) here
   
     #f is a file object
        return f.read()

def main():

    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    filename = sys.argv[1]

    #filename = "books/frankenstein.txt"
    output = get_book_text(filename)
    
    from stats import word_count
    count = word_count(output)
    #print(f"{count} words found in the document")

    from stats import character_count
    total_char = character_count(output)
    #print(f"{total_char}")

    from stats import dict_seperate
    complete_list = dict_seperate(total_char)
    #print(f"{complete_list}")

    from stats import sort_dict_list
    dict_list = sort_dict_list(complete_list)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in dict_list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")




 
main()

