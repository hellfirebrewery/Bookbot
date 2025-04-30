def word_count(output):
    count = output.split()
    num = len(count)
    return num

def character_count(output):
    char_count = {}
    out1 = output.lower()
    for char in out1:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count