from support_module import *


decryption_keys = {}


encryption_symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','@','#','$','%','&']


solution = []


def show_list_of_words(list_of_words, title):
    print(title.upper())
    for index in range(len(list_of_words)):
        print("{}. {}".format(index + 1, list_of_words[index]))


def verify_word_validity(word, list_of_valid_words):
    try:
        if len(word) < 2:
            raise Exception("")
        aux = list_of_valid_words[word.lower()]
        return True
    except:
        return False


def key_already_exists(keys, letter):
    try:
        aux = keys[letter]
        return True
    except:
        return False


def encrypt_words(orginal_list):
    
    encrypted_list = []
    encryption_keys = {}
    already_used_symbols = []

    for word in orginal_list:

        word_encrypted = ""
        for letter in word:

            if key_already_exists(encryption_keys, letter):
                word_encrypted += encryption_keys[letter]
            else:
                while True:
                    symbol = encryption_symbols[random.randint(0, len(encryption_symbols)-1)]
                    if symbol in already_used_symbols:
                        pass
                    else:
                        break
                already_used_symbols.append(symbol)
                encryption_keys[letter] = symbol
                word_encrypted += symbol
        
        encrypted_list.append(word_encrypted)

    return encrypted_list


def update_decryption_keys(current_keys, current_encrypted_word, current_real_word):
    pass


def get_key_from_value(dictionary, value):
    try:
        all_keys = list(dictionary.keys())
        all_values = list(dictionary.values())
        position = all_values.index(value)
        return all_keys[position]
    except ValueError as e:
        return None


def get_value_from_key(dictionary, key):
    return dictionary.get(key)


def decrypt_using_keys(word, keys):

    aux_word = ""

    list_of_keys = list(keys.keys())
    list_of_values = list(keys.values())

    for letter in word:
        if get_key_from_value(keys, letter) != None:
            aux_word += get_key_from_value(keys, letter)
        else:
            break

    return aux_word


def decryption_match(encrypted, real, keys):
    if get_value_from_key(keys, real) == encrypted and get_key_from_value(keys, encrypted) == real:
        return 'match'
    else:
        if real in keys:
            return 'no_match'
        else:
            if not (encrypted in keys.values()):
                return 'create_key'
            else:
                return 'no_match'



def trial_and_error_method(encrypted_word_list, current_encrypted_word_index, list_of_valid_words, words_grouped_by_lenght, current_decryption_keys):

    global solution

    if current_encrypted_word_index == 0 and len(solution) > 0:
        solution = []

    initial_keys_state = current_decryption_keys.copy()

    current_real_word_index = 0

    while True:
        
        try:
            current_backup_of_keys = current_decryption_keys.copy()
            current_encrypted_word = encrypted_word_list[current_encrypted_word_index]
            array_of_matching_lenght = words_grouped_by_lenght[len(current_encrypted_word)]
            current_real_word = array_of_matching_lenght[current_real_word_index]
            encrypted_word_matches_keys = True
        except Exception as e:
            print("BIG ERROR OCURRED: ",e)
            pass

        for index in range(len(current_encrypted_word)):
            
            matching_results = decryption_match(current_encrypted_word[index], current_real_word[index], current_backup_of_keys)

            if matching_results == "no_match":
                encrypted_word_matches_keys = False


            if matching_results == "create_key":
                current_backup_of_keys[current_real_word[index]] = current_encrypted_word[index]
        
        possible_result = decrypt_using_keys(current_encrypted_word, current_backup_of_keys)

        word_exist = verify_word_validity(possible_result, list_of_valid_words)


        if word_exist and encrypted_word_matches_keys:
            
            solution.append(current_real_word)

            if current_encrypted_word_index+1 < len(encrypted_word_list):
                trial_and_error_method(encrypted_word_list, current_encrypted_word_index+1, list_of_valid_words, words_grouped_by_lenght, current_backup_of_keys)

            if len(solution) < len(encrypted_word_list):
                current_real_word_index +=1
                current_backup_of_keys = initial_keys_state.copy()
                solution.pop()
                if current_real_word_index == len(array_of_matching_lenght):
                    break
                continue
            
            if len(solution) == len(encrypted_word_list) and current_encrypted_word_index+1 == len(encrypted_word_list):
                print("GENERATED DECRYPTION KEYS")
                print(current_backup_of_keys)

            if len(solution) == len(encrypted_word_list) and current_encrypted_word_index == 0:
                return solution

            break
        else:
            current_real_word_index +=1
            current_backup_of_keys = initial_keys_state.copy()
            if current_real_word_index == len(array_of_matching_lenght):
                break


def patterns_method(encrypted_word_list, list_of_valid_words):
    return []