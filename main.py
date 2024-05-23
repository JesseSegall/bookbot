def main():
    path = "books/frankenstein.txt"
    book = get_text(path)
    count = word_count(book)
    dictionary = count_letters(book)
    sorted = sort_dict_by_keys(dictionary)
    report(sorted, path, count)


def get_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)


def report(sorted_dict, path, count):
    print(f"Report of {path}")
    print(f"{count} words were found in the document")

    for key, value in sorted_dict.items():
        print(f"The '{key}' character was found {value} times ")
    print("End of Report")


def sort_dict_by_keys(dictionary):
    sorted_keys = sorted(dictionary.keys())
    sorted_dict = {key: dictionary[key] for key in sorted_keys}
    return sorted_dict


def count_letters(text):
    letters = {}
    text_l = text.lower()
    for letter in text_l:
        if letter.isalpha():
            letters[letter] = letters.get(letter, 0) + 1
    return letters


if __name__ == '__main__':
    main()
