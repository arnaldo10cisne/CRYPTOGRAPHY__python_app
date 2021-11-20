from support_module import *
from functions_module import *


def exit_program():
    print("""
    Thank you for using the Cryptography App.
    Have a wonderful day! 
    
    Press ENTER to exit""")

def menu ():
    return int(input("""
                                                                
   (                     )                            )      
   )\  (   (          ( /(     (  ( (      )       ( /((     
 (((_) )(  )\ ) `  )  )\())(   )\))()(  ( /( `  )  )\())\ )  
 )\___(()\(()/( /(/( (_))/ )\ ((_))(()\ )(_))/(/( ((_)(()/(  
((/ __|((_))(_)|(_)_\| |_ ((_) (()(_|(_|(_)_((_)_\| |(_)(_)) 
 | (__| '_| || | '_ \)  _/ _ \/ _` | '_/ _` | '_ \) ' \ || | 
  \___|_|  \_, | .__/ \__\___/\__, |_| \__,_| .__/|_||_\_, | 
           |__/|_|            |___/         |_|        |__/ 


    Welcome to the Cryptography App. Please select an option:

    1. Start this App
    2. About this App
    3. Exit
    Selection: """))


def run_app():
    """Main flow of the program. Here we call all the functions located in NBA_MODULE.PY"""
    
    LIST_OF_WORDS = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json'
    RANDOM_WORD_REQUEST = "https://random-word-api.herokuapp.com/word?number=1&swear=0"
    l(2)
    print("Please wait while we fetch the data from the URL ...")
    response = requests.get(LIST_OF_WORDS)

    #If the information is gathered correctly, the app is ready to start
    if response.status_code == 200:
        
        print("Data fetched succesfully!")
        l(1)
        
        #First we need to order the fetched array, so we are able to search for values on it.
        response_json_format = response.json()
        
        line(60)
        mode_selection = int(input("""\nWhat mode would you like to run?:\n \n1. Choose my own words to encrypt (Word validation will be applied)\n2. Choose randomly the words to encrypt\n\nSelection: """))
        l(1)
        line(60)

        word_list = []
        word_count = 0

        if mode_selection == 1:
            
            print("\nPlease enter words of at least 2 letters\n")
            while True:
                word = input("Next word ({} remaining): ".format(10-word_count))
                try:
                    if len(word) < 2:
                        raise Exception("The words must have more than 2 letters")
                    aux = response_json_format[word.lower()]
                    word_count += 1
                    word_list.append(word.lower())
                except:
                    print("Not a vaid word, please choose another one")
                if word_count == 10:
                    break
            
            print(word_list)

        
        elif mode_selection == 2:

            print("\nGetting random words from the internet, please wait...")
            
            while True:
                word = requests.get(RANDOM_WORD_REQUEST).json()[0]
                try:
                    if len(word) < 2:
                        raise Exception("")
                    aux = response_json_format[word.lower()]
                    word_count += 1
                    word_list.append(word.lower())
                except:
                    pass
                if word_count == 10:
                    l(2)
                    break

            print(word_list)

        
        encrypted_word_list = encrypt_words(word_list)

        print(encrypted_word_list)


    elif response.status_code >= 400:
        print("Error")

    standby()


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