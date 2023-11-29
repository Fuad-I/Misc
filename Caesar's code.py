def shift(word, number):
    return ''.join(chr(ord(letter) + number) for letter in word)


def find_shift_number(text, known_word):
    word_list = text.split()
    for item in filter(lambda x: len(x) == len(known_word), word_list):
        for i in range(26):
            if shift(item, i) == known_word:
                return i

    return 0


def decode(text, known_word):
    num = find_shift_number(text, known_word)
    return ' '.join(shift(word, num) for word in text.split())


def encode(text, shift_num):
    return ' '.join(shift(word, shift_num) for word in text.split())


original_text = 'hello darkness my old friend'
shift_number = -2
encoded_text = encode(original_text, shift_number)
print(encoded_text)
decoded_text = decode(encoded_text, 'my')
print(decoded_text)
