def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
        wordlist = file_contents.split()
        num_words = len(wordlist)
    return print(f"Found {num_words} total words")

def character_count(path):
    with open(path) as f:
        chars = {}
        file_contents = f.read()
        file_contents = file_contents.lower()
        character_list = list(file_contents)
        for char in character_list:
            if char in chars:
                chars[char] += 1
            if char not in chars:
                chars[char] = 1
        #letters.sort(reversed=True, key=char)
        return (chars)
    
def sort_on(items):
    return items["num"]

def sorted_list(chars):
    letters = []
    sorted_letters = {}
    for char in chars:
        if char.isalpha() == True:
            letters.append({
                "letter" : char ,
                "num" : chars[char]
            })
    letters.sort(key = sort_on, reverse=True)
    for letter in letters:
        print(f"{letter["letter"]}:",chars[letter["letter"]])
    return