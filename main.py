def main():
    from stats import get_num_words
    from stats import character_count
    from stats import sorted_list
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    
    get_num_words(path)

    print ("--------- Character Count -------")

    sorted_list(character_count(path))

    print('============= END ===============')

main()
