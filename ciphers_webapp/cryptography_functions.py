def rail_fence_encrypt(text, rows):

    text = text.upper().replace(" ", "")
    columns = len(text)

    if columns <= 1 or rows <= 1 or rows >= columns:
        return text

    lst = [[""] * columns for _ in range(rows)]

    i, j = 0, 0

    down = False

    while i < columns:
        lst[j][i] = text[i]

        if j == 0 or j == rows - 1:
            down = not down

        j += 1 if down else -1
        i += 1

    return "".join("".join(sublist) for sublist in lst)
 

def rail_fence_decrypt(text, rows):
    columns = len(text)

    if columns <= 1 or rows <= 1 or rows >= columns:
        return text

    lst = [[""] * columns for _ in range(rows)]

    i, j = 0, 0
    down = False
    while i < columns:
        lst[j][i] = True

        if j == 0 or j == rows - 1:
            down = not down

        j += 1 if down else -1
        i += 1

    char_index = 0
    for sublist in lst:
        for index in range(len(sublist)):
            if sublist[index]:
                sublist[index] = text[char_index]
                char_index += 1


    i, j = 0, 0
    down = False
    decrypted_text = ""
    while i < columns:
        decrypted_text += lst[j][i]

        if j == 0 or j == rows - 1:
            down = not down

        j += 1 if down else -1
        i += 1

    return decrypted_text


def vigenere_cipher(text, key, encrypt=True):
    ascii_lower_offsite = ord("a")
    ascii_upper_offsite = ord("A")

    key = key.replace(" ", "")
    key_length = len(key)
    key_index = 0

    res = ""

    for char in text:
        if char == " ":
            res += char

        else:
            shift = ord(key[key_index % key_length]) if encrypt else -ord(key[key_index % key_length])

            if char.isupper():

                res += chr((ord(char) + shift - ascii_upper_offsite) % 26 + ascii_upper_offsite)
            else:
                res += chr((ord(char) + shift - ascii_lower_offsite) % 26 + ascii_lower_offsite)

            key_index += 1

    return res
