def text_stats_report(word_count, char_freq):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()

    # sort the dictionary
    char_freq_dict = {
        char: count
        for char, count in sorted(
            char_freq.items(), key=lambda item: item[1], reverse=True
        )
    }

    for char, freq in char_freq_dict.items():
        print(f"The '{char}' was found {freq} times")
    print("--- End report ---")


def count_characters(text):
    char_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_dict.keys():
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    return char_dict


def split_text_into_list(text):
    return text.split()


def text_word_count(text):
    return len(split_text_into_list(text))


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    text_stats_report(text_word_count(file_contents), count_characters(file_contents))


if __name__ == "__main__":
    main()
