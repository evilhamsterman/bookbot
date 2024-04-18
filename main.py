def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    print(f"--- Begin report of {file_path} ---")
    print(f"{count_words(file_contents)} words in found in the document\n")
    chars_count = count_chars(file_contents)
    chars = sort_dict_keys(chars_count)
    for k in chars:
        if k.isalpha():
            print(f"The '{k}' character was found {chars_count[k]} times")


def sort_dict_keys(d: dict) -> list[str]:
    l = []
    for k in d:
        l.append(k)
    l.sort()
    return l


def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> dict[int]:
    text = text.lower()
    chars = {}
    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


if __name__ == "__main__":
    main()
