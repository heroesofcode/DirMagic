import requests
import sys
import dns.resolver

def header():
    print("""
            _______   __  .______         .___  ___.      ___       _______  __    ______ 
        |       \ |  | |   _  \        |   \/   |     /   \     /  _____||  |  /      |
        |  .--.  ||  | |  |_)  |       |  \  /  |    /  ^  \   |  |  __  |  | |  ,----'
        |  |  |  ||  | |      /        |  |\/|  |   /  /_\  \  |  | |_ | |  | |  |     
        |  '--'  ||  | |  |\  \----.   |  |  |  |  /  _____  \ |  |__| | |  | |  `----.
        |_______/ |__| | _| `._____|   |__|  |__| /__/     \__\ \______| |__|  \______|

        About: Bkakdkakdkdkk
        Author: João Lucas
        Language: Python
        GitHub: https://github.com/joaolfp/DirMagic                                                                              
    """)

def find_dir():
    try:
        print("\n")
        url = input("URL: ")
        wordlist = input("WordList: ")

        print("\n -------------- search .... --------------")

        with open(wordlist, "r") as file:
            directories = file.readlines()

        for directory in directories:
            directory = directory.strip()
            response = requests.get(url+directory)

            if response.status_code != 404:
                print("{} - {}".format(url+directory, response.status_code))
    except KeyboardInterrupt:
        print("\n Bye!!!")
        sys.exit()
    except:
        print("an error happened")
        sys.exit()

def find_dns():
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

                for response in responses:
                    print("{}, {}".format(subdomain, response))
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
    print("2 - Find DNS \n")
    
    try:
        item = input("Choose some of the options: ")
        
        if item == "1":
            find_dir()
        elif item == "2":
            find_dns()
        else:
            print("This option does not exist")
    except KeyboardInterrupt:
        print("\n Bye!!!")
        sys.exit()