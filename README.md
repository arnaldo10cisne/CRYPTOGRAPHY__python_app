
![Main menu](https://res.cloudinary.com/arnaldo10cisne/image/upload/v1637513577/cryptography_app/crypto1_vo8wqt.png)

# Cryptography App

I got inspired to develop this program because it was a test that was given to me in a technical interview. I wasn't sure how to do it back then, so I decided to give it a try. It can encrypt and decrypt arrays of English words. The word API used to validate words and obtain random ones is  [https://random-word-api.herokuapp.com](https://random-word-api.herokuapp.com/)
    
![App capture 1](https://res.cloudinary.com/arnaldo10cisne/image/upload/v1637514080/cryptography_app/crypto3_s9w5wd.png)
![App capture 2](https://res.cloudinary.com/arnaldo10cisne/image/upload/v1637514080/cryptography_app/crypto3_s9w5wd.png)



## How to use:
This repository contains the following ".py" files. You'll need all three of them to run this program:

- **main**:  This is the file where you'll find the rendering of the main menu, and each of the options it contains. It will also do the calls to all the functions that will make this program work.
- **functions_module**: Here, you’ll find the most important functions that will help encrypt and decrypt words, validate that a word exists using the words API, and show information to the user in an easily readable state.
- **support_module**: This module includes all the imports that the program needs to work, and some auxiliary functions to help with aesthetics.

### Running the code:

You can run this application following the next steps:

1.  First, you have to make sure that you have Python installed on your computer. If you are not quite sure if Python is installed on your computer, please go to the command line and type `python3 --version` if you are on Linux or Mac, or `python --version` if you are on Windows. You should be given the current version of Python installed on your computer. If an error message pops up saying that the command was not recognized, most likely you need to install Python. To do so, please follow [this](www.m.com) tutorial.
 2. After Python has been successfully installed, the next step is very simple. You need to download this repository in a ZIP file
	 - ![Downloading ZIP](https://res.cloudinary.com/arnaldo10cisne/image/upload/v1637514119/cryptography_app/crypto4_evij2t.png)
 3. Once you have all files, locate them on a single directory, and make sure to run the file **"main .py"**. If you have all files in the same directory, the app should run without any issues.
 4. If the program doesn't start, however, make sure you have the "request" module installed. This module is required for python to fetch the data from the URL. To install this module, inside the command line execute the following command: `pip install requests` 

### Suggestions

Any suggestion you have on how to improve this project can be submitted using the  [contact form in my personal website](https://www.arnaldocisneros.com/contact).