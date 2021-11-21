import requests
import json
import os
import random


def clear_screen():
        """Function created to clean the console, to provide a better experience. It needs to evaluate the OS first."""
        if os.name=="nt":
                os.system("cls")
        else:
                os.system("clear")


def l(n):
        """Function created to create a new empty line, to provide a better experience"""
        for i in range(n): print("")


def standby(): 
        """Function created to pause the program until the user presses ENTER, to provide a better experience"""
        a=input()


def line(n):
	for i in range(n): print("-", end="");
	print("")