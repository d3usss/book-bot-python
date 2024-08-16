def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print("\n")
    
    letters = count_letters(file_contents)
    
    for key, value in letters.items():
        print_letter_count(key, value)
    
    print("--- End report ---")
        
def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_letters(file_contents):
    lowered_file_contents = file_contents.lower()
    return {
        "a": lowered_file_contents.count("a"),
        "b": lowered_file_contents.count("b"),
        "c": lowered_file_contents.count("c"),
        "d": lowered_file_contents.count("d"),
        "e": lowered_file_contents.count("e"),
        "f": lowered_file_contents.count("f"),
        "g": lowered_file_contents.count("g"),
        "h": lowered_file_contents.count("h"),
        "i": lowered_file_contents.count("i"),
        "j": lowered_file_contents.count("j"),
        "k": lowered_file_contents.count("k"),
        "l": lowered_file_contents.count("l"),
        "m": lowered_file_contents.count("m"),
        "n": lowered_file_contents.count("n"),
        "o": lowered_file_contents.count("o"),
        "p": lowered_file_contents.count("p"),
        "q": lowered_file_contents.count("q"),
        "r": lowered_file_contents.count("r"),
        "s": lowered_file_contents.count("s"),
        "t": lowered_file_contents.count("t"),
        "u": lowered_file_contents.count("u"),
        "v": lowered_file_contents.count("v"),
        "w": lowered_file_contents.count("w"),
        "x": lowered_file_contents.count("x"),
        "y": lowered_file_contents.count("y"),
        "z": lowered_file_contents.count("z"),
    }

def print_letter_count(letter, count):
    print(f"The '{letter}' character was found {count} times")
        
main()