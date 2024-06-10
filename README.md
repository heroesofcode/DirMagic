# DirMagic

[![Testing](https://github.com/heroesofcode/DirMagic/actions/workflows/Testing.yml/badge.svg)](https://github.com/heroesofcode/DirMagic/actions/workflows/Testing.yml)
[![Python 3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/)
[![GitHub](https://img.shields.io/github/license/heroesofcode/DirMagic)](https://github.com/joaolfp/DirMagic/blob/master/LICENSE)

DirMagic is a library written in Python to brute force directories and subdomains

## Installation
```
git clone https://github.com/heroesofcode/DirMagic.git
```

## Usage

```
cd DirMagic
pip install -r requirements.txt
python3 dirMagic.py
```

1 - Find directories

<img src="https://github.com/heroesofcode/DirMagic/blob/master/assets/dir.png">

2 - Find subdomains

<img src="https://github.com/heroesofcode/DirMagic/blob/master/assets/subdomain.png">

### WordLists

You can create your own wordlist with .txt, follow the example below

wordlist.txt
```
admin
login
dashboard
blog
```

Below are some WordList links for downloads

- If you're running on [Kali Linux](https://www.kali.org/), it's already installed on the system, just follow this [documentation](https://www.kali.org/tools/wordlists/).
- [SecLists](https://github.com/danielmiessler/SecLists) is a repository that has several wordlists to download.

## Contribution

* To contribute, from a fork in the project please feel free to give suggestions, improvements and feel free to add features. After you contribute, open a pull request.

## Contributors

<a href="https://github.com/heroesofcode/DirMagic/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=heroesofcode/DirMagic" />
</a>

## License
DirMagic is released under the MIT license. See [LICENSE](https://github.com/heroesofcode/DirMagic/blob/master/LICENSE) for details.
