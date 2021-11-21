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
    
    for index in range(current_encrypted_word):
        
        # Without replacing existing keys
        
        # try:
        #     aux = current_keys[current_real_word[index]]
        # except:
        #     current_keys[current_real_word[index]] = current_encrypted_word[index]

        # Replacing existing keys

        current_keys[current_real_word[index]] = current_encrypted_word[index]
    
    return current_keys


def get_key_from_value(dictionary, value):
    try:
        print("get_key_from_value | dictionary={} , value={}".format(dictionary,value))
        print("subfunc entro 1")
        all_keys = list(dictionary.keys())
        print("subfunc entro 2")
        all_values = list(dictionary.values())
        print(all_keys)
        print(all_values)
        print("subfunc entro 3 | all_values={}, value={}".format(all_values,value))
        position = all_values.index(value)
        print("subfunc entro 4")
        return all_keys[position]
    except ValueError as e:
        print(e)
        return None


def get_value_from_key(dictionary, key):
    return dictionary.get(key)


def decrypt_using_keys(word, keys):
    
    print("Funtion entro 1")
    print("decrypt_using_keys | word={} | keys={}".format(word,keys))

    aux_word = ""

    list_of_keys = list(keys.keys())
    list_of_values = list(keys.values())

    print("Funtion entro 2")

    for letter in word:
        print("Funtion entro 3 | letter={}".format(letter))
        if get_key_from_value(keys, letter) != None:
            aux_word += get_key_from_value(keys, letter)
        else:
            break
        print("Funtion entro 4, aux_word={}".format(aux_word))

    print("Funtion entro 5")
    return aux_word


def word_matches_current_keys(word, keys):
    #Returns TRUE if the word can be a solution for the current keys, or FALSE if it can't
    pass


# def trial_and_error_method(encrypted_word_list, current_encrypted_word_index, list_of_valid_words, words_grouped_by_lenght, go_back):
    
#     #Index for the array of real words, where we are going to evaluate one by one
#     current_word_evaluated = 0

#     if go_back:
#         print("PENDIENTE")
#         return None
#     else:
#         while True:
            
#             # WE UPDATE THE DECRYPTION KEYS WITH THE LETTERS OF THE NEW WORD
#             decryption_keys = update_decryption_keys(decryption_keys, encrypted_word_list[current_encrypted_word_index], words_grouped_by_lenght[len(encrypted_word_list[current_encrypted_word_index])][current_word_evaluated])

#             word_to_evaluate = decrypt_using_keys(encrypted_word_list[current_encrypted_word_index], decryption_keys)

#             if verify_word_validity(word_to_evaluate, list_of_valid_words):
#                 solution.append(word_to_evaluate)
#                 if len(solution) < len(encrypted_word_list):
#                     trial_and_error_method(encrypted_word_list, current_encrypted_word_index+1, list_of_valid_words, words_grouped_by_lenght, False)
#                     #PENDIENTE: Evaluar si la cantidad de palabras en solution es igual a la cantidad de palabras en encrypted word list
#                 else:
#                     return solution
#             else:
#                 current_word_evaluated += 1
#                 if current_word_evaluated < len(words_grouped_by_lenght[len(encrypted_word_list[current_encrypted_word_index])]):
#                     continue
#                 else:
#                     return None
                
#                 print("PENDIENTE")
#                 print("bad")


def decryption_match(encrypted, real, keys):
    if get_value_from_key(keys, real) == encrypted and get_key_from_value(keys, encrypted) == real:
        return 'match'
    else:
        if real in keys:
            return 'no_match'
        else:
            if encrypted in keys.values():
                return 'duplicate_key_error'
            else:
                return 'create_key'



def trial_and_error_method(encrypted_word_list, current_encrypted_word_index, list_of_valid_words, words_grouped_by_lenght, go_back):

    current_real_word_index = 0

    print("Entro 0")

    while True:

        print("Entro 1")
        
        try:
            current_backup_of_keys = decryption_keys.copy()
            print("INITIAL CURRENT BACKUP KEYS = {}".format(current_backup_of_keys))
            print("DECRYPTION KEYS = {}".format(decryption_keys))
            current_encrypted_word = encrypted_word_list[current_encrypted_word_index]
            array_of_matching_lenght = words_grouped_by_lenght[len(current_encrypted_word)]
            current_real_word = array_of_matching_lenght[current_real_word_index]
            encrypted_word_matches_keys = True
        except Exception as e:
            print(e)

        print("Entro 2, comparing {} with {}".format(current_encrypted_word,current_real_word))

        for index in range(len(current_encrypted_word)):

            print("Entro 3, index={}, eL={}, rL={}".format(index,current_encrypted_word[index],current_real_word[index]))
            
            #Returns 'match' if the 2 letters match with current keys, 'no_match' if they don't match, and 'create_key' if the key is not present a needs to be created
            matching_results = decryption_match(current_encrypted_word[index], current_real_word[index], current_backup_of_keys)

            print("Entro 4")

            if matching_results == "no_match":
                # encrypted_word_matches_keys = False
                print("Entro 5")
                encrypted_word_matches_keys = False


            if matching_results == "create_key":
                current_backup_of_keys[current_real_word[index]] = current_encrypted_word[index]
                print("Entro 6")

            if matching_results == 'duplicate_key_error':
                print("AN ERROR OCURRED, DUPLICATE VALUES IN THE KEYS, current_real_word_index= {}".format(current_real_word_index))

        print("Entro 6.5")
        
        possible_result = decrypt_using_keys(current_encrypted_word, current_backup_of_keys)

        print("Entro 6.75")

        word_exist = verify_word_validity(possible_result, list_of_valid_words)

        print("Entro 7")

        if word_exist and encrypted_word_matches_keys:
            #WE CALL THE NEXT ITERATION OF RECURSIVE METHOD HERE
            print("Entro 8")
            print("Found match")
            print("{} matches with {}".format(current_encrypted_word, current_real_word))
            current_backup_of_keys = {}
            
            break
        else:
            current_real_word_index +=1
            current_backup_of_keys = {}
            print("ENDING DECRYPTION KEYS = {}".format(decryption_keys))
            print("Entro 9")






def patterns_method(encrypted_word_list, list_of_valid_words):
    return []