import requests
import sys
import dns.resolver
from rich.console import Console

class DirMagic(object):

    def find_dir(self):
        try:
            print("\n")
            url = input("URL: ")
            wordlist = input("WordList: ")

            console = Console()
            console.print("\n -------------- search .... --------------", style="#af00ff")

            all_results = []

            with open(wordlist, "r") as file:
                directories = file.readlines()

            for directory in directories:
                directory = directory.strip()
                response = requests.get(url + directory)

                if response.status_code != 404:
                    print("{} - {}".format(url + directory, response.status_code))
                    all_results.append("{} - {}".format(url + directory, response.status_code))

            with open("directories_found.txt", 'w') as file:
                for item in all_results:
                    file.write("{}\n".format(item))
            
            console.print("Saved in the directories_found.txt file", style="#008000")
        except KeyboardInterrupt:
            print("\n Bye!!!")
            sys.exit()
        except Exception as e:
            print(f"An error happened: {e}")
            sys.exit()

    def test_subdomain(self, subdomain):
        try:
            resolver = dns.resolver.Resolver()
            responses = resolver.resolve(subdomain, "A")
            return True
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
            return False
        except Exception as e:
            print(f"An error happened: {e}")
            return False

    def find_subdomains(self):
        try:
            print("\n")
            domain = input("Domain: ")
            wordlist = input("WordList: ")

            console = Console()
            console.print("\n -------------- search --------------", style="#af00ff")

            all_results = []

            with open(wordlist, "r") as file:
                words = file.read().splitlines()

            for word in words:
                subdomain = "{}.{}".format(word, domain)

                if self.test_subdomain(subdomain):
                    try:
                        response = requests.get("http://" + subdomain)
                        if response.status_code != 404:
                            print("{}".format(subdomain))
                            all_results.append(subdomain)
                    except requests.RequestException as e:
                        print(f"Failed to request {subdomain}: {e}")

            with open("subdomains_found.txt", 'w') as file:
                for item in all_results:
                    file.write("{}\n".format(item))
                    
            console.print("Saved in the subdomains_found.txt file", style="#008000")
        except KeyboardInterrupt:
            print("\n Bye!!!")
            sys.exit()
        except Exception as e:
            print(f"An error happened: {e}")
            sys.exit()