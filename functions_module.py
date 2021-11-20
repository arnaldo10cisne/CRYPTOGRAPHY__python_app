def key_already_exists(keys, letter):
    pass


def encrypt_words(orginal_list):
    
    encrypted_list = []
    encryption_keys = {}

    for word in orginal_list:

        word_encrypted = ""
        for letter in word:

            if key_already_exists(encryption_keys, letter):
                word_encrypted.append(encryption_keys[letter])
            else:
                pass
                # get_random_character(encryption_keys, letter)
                # word_encrypted.append(encryption_keys[letter])


    return encrypted_list