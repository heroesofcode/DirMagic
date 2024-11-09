import sys
from dir_magic.header import Header
from dir_magic.dirMagic import DirMagic

if __name__ == "__main__":
    Header().setup()
    dir_magic = DirMagic()

    print("1 - Find Directories")
    print("2 - Find Subdomains \n")
    
    try:
        item = input("Choose some of the options: ")
        
        if item == "1":
            dir_magic.find_dir()
        elif item == "2":
            dir_magic.find_subdomains()
        else:
            print("This option does not exist")
    except KeyboardInterrupt:
        print("\n Bye!!!")
        sys.exit()