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
    
    LIST_OF_WORDS = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json'
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
        mode_selection = int(input("""\nWhat mode would you like to run?:\n \n1. Choose my own words to encrypt (Word validation will be applied)\n2. Choose random words to encrypt\n\nSelection: """))
        l(1)
        line(60)

        word_list = []
        word_count = 0

        if mode_selection == 1:
            
            print("\nPlease enter words of at least 2 letters\n")
            while True:
                word = input("Next word ({} remaining): ".format(3-word_count))
                if (verify_word_validity(word, response_json_format)):
                    word_count += 1
                    word_list.append(word.lower())
                else:
                    print("Not a vaid word, please choose another one")
                if word_count == 3:
                    l(1)
                    break

        elif mode_selection == 2:

            print("\nGetting random words from the internet, please wait...")
            
            while True:
                word = requests.get(RANDOM_WORD_REQUEST).json()[0]
                if (verify_word_validity(word, response_json_format)):
                    word_count += 1
                    word_list.append(word.lower())
                else:
                    pass
                if word_count == 3:
                    l(1)
                    break

        show_list_of_words(word_list, "List of chosen words")
        
        encrypted_word_list = encrypt_words(word_list)

        show_list_of_words(encrypted_word_list, "\nEncryption applied")

        l(1)
        line(60)

        decryption_method = int(input("""\nWhat decryption method would you like to use?:\n(More information about the 2 methods in the ABOUT section on the main menu)\n\n1. Trial and error\n2. Looking for patterns (CURRENTLY UNAVAILABLE)\n\nSelection: """))
        l(1)
        line(60)
        print("\nDecrypting words, please wait...\n")

        if decryption_method == 1:
            
            words_grouped_by_lenght = {}
            
            for word in response_json_format:
                try:
                    aux = words_grouped_by_lenght[len(word)]
                    words_grouped_by_lenght[len(word)].append(word)
                except:
                    words_grouped_by_lenght[len(word)] = []
                    words_grouped_by_lenght[len(word)].append(word)

            possible_solution = trial_and_error_method(encrypted_word_list, 0, response_json_format, words_grouped_by_lenght, {})

        elif decryption_method == 2:
            
            possible_solution = patterns_method(encrypted_word_list, response_json_format)

        print("\nShowing possible solution\n(The result may be different from the original words)")
        show_list_of_words(encrypted_word_list, "\nEncrypted words:")
        show_list_of_words(possible_solution, "\nDecrypted words:")

        print("\nThank you for using the Cryptography App! Returning to the main menu")


    elif response.status_code >= 400:
        print("Error")

    standby()


def about():
    print("""
    
    Program created by Arnaldo Cisneros. I got inspired to develop it because it was a test that was given
    to me in a technical interview. I wasn't sure how to do it back then, but every time we are faced with
    a problem that we don't know how to solve, but do it anyway, we become a better person.
    
    This program can encrypt and decrypt arrays of English words.
    
    The ENCRYPTION process is very straightforward. We just need to change each of the letters in the array
    to a new one, creating an encryption key in the process to make the changes consistent.
    
    This way, if we have the following array of words:
    --> ['selfish','fish','fishing','jellyfish'] <--
    We can change each of the letters for another random symbol, creating the following encryption guide: 
    
    ('->' = 'becomes')
    | S -> M | E -> W | L -> P | F -> R |
    | I -> N | H -> F | N -> Q | G -> K |
             | J -> $ | Y -> # |
    
    At the end of the encryption process, we'll have the following encrypted array, ready to be decrypted:
    --> ['mwprnmf','rnmf','rnmfnqk','$wpp#rnmf'] <--

    The DECRYPTION process is more complex, and the algorithm used here is a simple trial and error with a
    recursive function. First, we need to separate all the valid english words in number of characters. 
    This way, we'll have a structure similar to this one:

    1 : ['a','e','i','o','u', ...]
    2 : ['me','he','it','we','us', ...]
    3 : ['him','you','red','win','boy', ...]
    4 : ['girl','ways','lego','cold','moon', ...]
    ....

    Then, we'll go over each of the encrypted words and assign them to the ones that have the same amount of 
    characters, creating a possible encryption guide during the process.  
    If we run out of possible matches on one word, we go back to the previous one, and find the next possible 
    result, changing the encryption guide until we have one that gives good results on all the encrypted words.

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