import numpy as np

WHITESPACE = ' '
ZERO = '0'
ONE = '1'
PRINTABLE_CHAR = '#'
NON_PRINTABLE_CHAR = ' '

letters_mask_dict = {
    "a": np.array([[1, 0, 0, 1], [0, 1, 1, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]]),
    "b": np.array([[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 0, 1]]),
    "c": np.array([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [0, 1, 1, 0], [1, 0, 0, 1]]),
    "d": np.array([[0, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]),
    "e": np.array([[0, 0, 0], [0, 1, 1], [0, 0, 0], [0, 1, 1], [0, 0, 0]]),
    "f": np.array([[0, 0, 0], [0, 1, 1], [0, 0, 0], [0, 1, 1], [0, 1, 1]]),
    "g": np.array([[0, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 0, 1]]),
    "h": np.array([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]]),
    "i": np.array([0] * 5).reshape((5, 1)),
    "j": np.array([[1, 1, 0], [1, 1, 0], [1, 1, 0], [0, 1, 0], [1, 0, 1]]),
    "k": np.array([[0, 1, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]),
    "l": np.array([[0, 1, 1], [0, 1, 1], [0, 1, 1], [0, 1, 1], [0, 0, 0]]),
    "m": np.array([[0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]),
    "n": np.array([[0, 1, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]]),
    "o": np.array([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]),
    "p": np.array([[1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [1, 0, 1, 1], [1, 0, 1, 1]]),
    "q": np.array([[0, 0, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 0, 0]]),
    "r": np.array([[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0]]),
    "s": np.array([[1, 0, 0, 0], [0, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 0], [0, 0, 0, 1]]),
    "t": np.array([[0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]]),
    "u": np.array([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]),
    "v": np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 0, 1]]),
    "w": np.array([[0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0]]),
    "x": np.array([[0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0]]),
    "y": np.array([[0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1]]),
    "z": np.array([[0, 0, 0, 0, 0], [1, 1, 1, 0, 1], [1, 1, 0, 1, 1], [1, 0, 1, 1, 0], [0, 0, 0, 0, 0]])
}

def get_letter(letter) -> str:
    if letter == WHITESPACE:
        return np.array([WHITESPACE] * 5).reshape((5, 1))

    if letters_mask_dict[str.lower(letter)].any():
        list = letters_mask_dict[str.lower(letter)].astype(dtype=np.str)
        list[list == ZERO] = PRINTABLE_CHAR
        list[list == ONE] = NON_PRINTABLE_CHAR

        return list

def get_word(word) -> str:
    result = np.array([''] * 5).astype(np.str).reshape((5, 1))
    for i, letter in enumerate(word):
        fake = np.array([''] * 5).astype(np.str).reshape((5, 1))
        letter_with_whitespace = np.append(get_letter(letter),
                                           get_letter(WHITESPACE) if i + 1 != len(word) else fake,
                                           axis=1)
        result = np.append(result, letter_with_whitespace, axis=1)
    return result

def print_pseudo_graph_word(word):
    handled_word = get_word(word=word)
    for char_list in handled_word:
        string = char_list.tolist()
        print(str("".join(string)))

print_pseudo_graph_word("Hello world")
