def encode(message: str, key: int):
    length_message = len(message)
    encrypted_message = ""
    for i in range(length_message):
        single_char = message[i]
        encrypt = ord(single_char) + key
        new_char = chr(encrypt)
        encrypted_message = encrypted_message + new_char
    return encrypted_message


def encode_better(message: str, key: str):
    length_message = len(message)
    length_key = len(key)
    elements = []
    for i in range(length_message):
        elements.append(message[i])
    key_elements = []
    for j in range(length_message):
        key_elements.append(key[j % length_key])
    encrypt_message = []
    for k in range(length_message):
        key_ordinal = ord(key_elements[k]) - 65
        message_ordinal = ord(message[k]) - 65
        encrypt_message_ordinal = (message_ordinal + key_ordinal) % 58
        encrypt_message_char = chr(encrypt_message_ordinal + 65)
        encrypt_message.append(encrypt_message_char)
    final_message = "".join(encrypt_message)
    return final_message