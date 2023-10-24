import requests
import sys
import dns.resolver
from rich.console import Console

def header():
    print("""
            _______   __  .______         .___  ___.      ___       _______  __    ______ 
        |       \ |  | |   _  \        |   \/   |     /   \     /  _____||  |  /      |
        |  .--.  ||  | |  |_)  |       |  \  /  |    /  ^  \   |  |  __  |  | |  ,----'
        |  |  |  ||  | |      /        |  |\/|  |   /  /_\  \  |  | |_ | |  | |  |     
        |  '--'  ||  | |  |\  \----.   |  |  |  |  /  _____  \ |  |__| | |  | |  `----.
        |_______/ |__| | _| `._____|   |__|  |__| /__/     \__\ \______| |__|  \______| (1.0.0)

        About: DirMagic is a library written in Python to brute force directories and subdomains
        Author: João Lucas
        Language: Python
        GitHub: https://github.com/heroesofcode/DirMagic                                                                            
    """)

def find_dir():
    try:
        print("\n")
        url = input("URL: ")
        wordlist = input("WordList: ")

        console = Console()
        console.print("\n -------------- search --------------", style="#af00ff")

        all_results = []

        with open(wordlist, "r") as file:
            directories = file.readlines()

        for directory in directories:
            directory = directory.strip()
            response = requests.get(url+directory)

            if response.status_code != 404:
                print("{} - {}".format(url+directory, response.status_code))
                all_results.append("{} - {}".format(url+directory, response.status_code))

        with open("directories_found.txt", 'w') as file:
            for item in all_results:
                file.write("{}\n".format(item))
        
        console.print("Saved in the directories_found.txt file", style="#008000")
    except KeyboardInterrupt:
        print("\n Bye!!!")
        sys.exit()
    except:
        print("an error happened")
        sys.exit()

def find_subdomains():
    try:
        print("\n")
        domain = input("Domain: ")
        wordlist = input("WordList: ")

        print("\n -------------- search --------------")

        with open(wordlist, "r") as file:
            words = file.read().splitlines()

        for word in words:
            subdomain = "{}.{}".format(word, domain)

            try:
                resolver = dns.resolver.Resolver()
                responses = resolver.resolve(subdomain, "A")
                print("{}".format(subdomain))
            except KeyboardInterrupt:
                print("\n Bye!!!")
                sys.exit()
            except:
                pass
    except KeyboardInterrupt:
        print("\n Bye!!!")
        sys.exit()
    except:
        print("an error happened")
        sys.exit()

if __name__ == "__main__":
    header()

    print("1 - Find Directories")
    print("2 - Find Subdomains \n")
    
    try:
        item = input("Choose some of the options: ")
        
        if item == "1":
            find_dir()
        elif item == "2":
            find_subdomains()
        else:
            print("This option does not exist")
    except KeyboardInterrupt:
        print("\n Bye!!!")
        sys.exit()
