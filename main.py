from support_module import *
from functions_module import *


def menu ():
    return int(input("""
                                                                    
       ______                 __                               __         
      / ____/______  ______  / /_____  ____ __________ _____  / /_  __  __
     / /   / ___/ / / / __ \/ __/ __ \/ __ `/ ___/ __ `/ __ \/ __ \/ / / /
    / /___/ /  / /_/ / /_/ / /_/ /_/ / /_/ / /  / /_/ / /_/ / / / / /_/ / 
    \____/_/   \__, / .___/\__/\____/\__, /_/   \__,_/ .___/_/ /_/\__, /  
              /____/_/              /____/          /_/_    ____ /____/   
                                                    /   |  / __ \/ __ \   
                                                   / /| | / /_/ / /_/ /   
                                                  / ___ |/ ____/ ____/    
                                                 /_/  |_/_/   /_/                                            
    
    Welcome to the Cryptography App. Please select an option:

    1. Start this App
    2. About this App
    3. Exit
    Selection: """))


def run_app():
    """Main flow of the program. Here we call all the functions located in FUNCTIONS_MODULE.PY"""
    
    # SECONDARY, SLOWER API
    #LIST_OF_WORDS = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json'
    
    LIST_OF_WORDS = 'https://random-word-api.herokuapp.com/all'
    RANDOM_WORD_REQUEST = "https://random-word-api.herokuapp.com/word?number=1&swear=0"
    l(2)
    print("Please wait while we fetch the data from the URL ...")
    response = requests.get(LIST_OF_WORDS)

    #If the information is gathered correctly, the app is ready to start
    if response.status_code == 200:
        
        print("Data fetched succesfully!")
        l(1)
        
        response_json_format = response.json()
        
        line(60)

        while True:
            try:
                number_of_words_chosen = int(input("\nHow many words would you like to encryt?: "))
                if number_of_words_chosen < 1:
                    raise Exception("")
                break
            except:
                pass

        while True:
            try:
                mode_selection = int(input("""\nWhat mode would you like to run?:\n \n1. Choose my own words to encrypt (Word validation will be applied)\n2. Choose random words to encrypt\n\nSelection: """))
                if mode_selection == 1 or mode_selection == 2:
                    break
                else:
                    raise Exception("")
            except:
                pass

        l(1)
        line(60)

        word_list = []
        word_count = 0

        if mode_selection == 1:
            
            print("\nPlease enter words of at least 2 letters\n")
            while True:
                word = input("Next word ({} remaining): ".format(number_of_words_chosen-word_count))
                if (verify_word_validity(word, response_json_format)):
                    word_count += 1
                    word_list.append(word.lower())
                else:
                    print("Not a vaid word, please choose another one")
                if word_count == number_of_words_chosen:
                    l(1)
                    break

        elif mode_selection == 2:

            print("\nGetting random words from the internet, please wait...")
            
            while True:
                word = requests.get(RANDOM_WORD_REQUEST).json()[0]
                word_count += 1
                word_list.append(word.lower())
                if word_count == number_of_words_chosen:
                    l(1)
                    break

        show_list_of_words(word_list, "List of chosen words")
        
        encrypted_word_list = encrypt_words(word_list)

        show_list_of_words(encrypted_word_list, "\nEncryption applied")

        l(1)
        line(60)

        while True:
            try:
                decryption_method = int(input("""\nWhat decryption method would you like to use?:\n\nNOTE: The decryption process is going to be from scratch.\nThe original words and keys are not going to be used.\nDepending on the words, the result may take a while\n\n1. Trial and error\n-. Looking for patterns (CURRENTLY UNAVAILABLE)\n\nSelection: """))
                if decryption_method != 1:
                    raise Exception("")
                else:
                    break
            except:
                pass

        l(1)
        line(60)
        print("\nDecrypting words, please wait...\n")

        if decryption_method == 1:
            
            words_grouped_by_lenght = {}
            
            for word in response_json_format:
                
                if len(word) in words_grouped_by_lenght:
                    words_grouped_by_lenght[len(word)].append(word)
                else:
                    words_grouped_by_lenght[len(word)] = []
                    words_grouped_by_lenght[len(word)].append(word)

            start_time = time.time()
            possible_solution, generated_decryption_keys = trial_and_error_method(encrypted_word_list, 0, response_json_format, words_grouped_by_lenght, {})
            end_time = time.time()

        # elif decryption_method == 2:
            
        #     possible_solution = patterns_method(encrypted_word_list, response_json_format)
        #     print("The patterns method is under construction. Please select the trial and error.")

        print("\nShowing possible solution\n(The result may be different from the original words)")
        show_list_of_words(encrypted_word_list, "\nEncrypted words:")
        print_pretty_keys(generated_decryption_keys, "\nGenerated decryption keys")
        show_list_of_words(possible_solution, "\n\nDecrypted words:")
        
        total_time = end_time - start_time
        number_of_words = len(possible_solution)
        number_of_characters = 0
        
        for word in possible_solution:
            for letter in word:
                number_of_characters += 1
        
        print("\nFINAL STATISTICS:\nDecryption time: {} seconds\nNumber of words: {}\nNumber of characters: {}\nNumber of Unique keys: {}".format(total_time,number_of_words,number_of_characters,len(list(generated_decryption_keys.keys()))))

        print("\nThank you for using the Cryptography App! Returning to the main menu")


    elif response.status_code >= 400:
        print("An error ocurred while fetching the information from the API. Please try again later")

    standby()


def about():
    print("""
    
    Program created by Arnaldo Cisneros. I got inspired to develop it because it was a test that was given
    to me in a technical interview. I wasn't sure how to do it back then, but every time we are faced with
    a problem that we don't know how to solve, but do it anyway, we become a better person.
    
    This program can encrypt and decrypt arrays of English words.
    

    ENCRYPTION
    ************************************************************************************************************
    |                                                                                                          |
    |  The ENCRYPTION process is very straightforward. We just need to change each of the letters in the array |
    |  to a new one, creating an encryption key in the process to make the changes consistent.                 |
    |                                                                                                          |
    |  This way, if we have the following array of words:                                                      |
    |  --> ['selfish','fish','fishing','jellyfish'] <--                                                        |
    |  We can change each of the letters for another random symbol, creating the following encryption guide:   |
    |                                                                                                          |
    |  ('->' = 'becomes')                                                                                      |
    |  | S -> M | E -> W | L -> P | F -> R |                                                                   |
    |  | I -> N | H -> F | N -> Q | G -> K |                                                                   |
    |           | J -> $ | Y -> # |                                                                            |
    |                                                                                                          |
    |  At the end of the encryption process, we'll have the following encrypted array, ready to be decrypted:  |
    |  --> ['mwprnmf','rnmf','rnmfnqk','$wpp#rnmf'] <--                                                        |
    |                                                                                                          |
    ************************************************************************************************************
    
    
    DECRYPTION
    ************************************************************************************************************
    |                                                                                                          |
    |  The DECRYPTION process is more complex, and the algorithm used here is a simple trial and error with a  |
    |  recursive function. First, we need to separate all the valid english words in number of characters.     |
    |  This way, we'll have a structure similar to this one:                                                   |
    |                                                                                                          |
    |  1 : ['a','e','i','o','u', ...]                                                                          |
    |  2 : ['me','he','it','we','us', ...]                                                                     |
    |  3 : ['him','you','red','win','boy', ...]                                                                |
    |  4 : ['girl','ways','lego','cold','moon', ...]                                                           |
    |  ....                                                                                                    |
    |                                                                                                          |
    |  Then, we'll go over each of the encrypted words and assign them to the ones that have the same amount   |
    |  of characters, creating a possible encryption guide during the process.                                 |
    |  If we run out of matches on a word, we go back to the previous one, and find the next possible result,  |
    |  changing the encryption guide until we have one that gives good results on all the encrypted words.     |
    |                                                                                                          |
    ************************************************************************************************************
    
    
    The word API used to validate words and obtain random ones is: https://random-word-api.herokuapp.com
    
    Developed in the city of Medellín, Colombia. November 2021.
    
    Visit me on my social media!
    Linekdin:         https://www.linkedin.com/in/arnaldo10cisne/
    Github:           https://github.com/arnaldo10cisne
    Personal website: https://www.arnaldocisneros.com/
    
    
    """)
    standby()


def exit_program():
    print("""
    Thank you for using the Cryptography App.
    Have a wonderful day! 
    
    Press ENTER to exit""")


if __name__ == "__main__":
    while True:
        try:
            clear_screen()
            opt = menu()
            if (opt==1):
                clear_screen()
                run_app()
            elif (opt==2):
                clear_screen()
                about()
            elif (opt==3):
                clear_screen()
                exit_program()
                standby()
                break
            else:
                pass
        except:
            pass
    clear_screen()