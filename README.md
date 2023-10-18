# WooCommerce Checker

![GitHub stars](https://img.shields.io/github/stars/ishanoshada/WooCommerce-Checker?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/ishanoshada/WooCommerce-Checker?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/ishanoshada/WooCommerce-Checker?style=flat-square)
![GitHub license](https://img.shields.io/github/license/ishanoshada/WooCommerce-Checker?style=flat-square)

WooCommerce Checker is a Python script designed to check if WooCommerce is installed on WordPress websites. It uses the `requests` library for making HTTP requests and provides a simple command-line interface for input.


## Features

- Automatically checks multiple WordPress login URLs with corresponding usernames and passwords.
- Logs successful logins and WooCommerce installations for further analysis.
- Utilizes multiprocessing for concurrent URL checking.

## Table of Contents

- [Usage](#usage)
- [Installation](#installation)
- [How to Contribute](#how-to-contribute)
- [License](#license)

## Usage

1. Create a text file named `logins.txt` containing WordPress login URLs along with usernames and passwords, separated by '|'. For example:

```
http://norwardstour.com/wp-login.php|db_kc|o^R50r4b
https://mrprinto.com/wp-login.php|preview|432432432
...
```

2. Run the script and provide the path to the input file.
3. The script will attempt to log in and check for WooCommerce installations.

```bash
python woocommerce_checker.py logins.txt
```


> Note: This script is for educational purposes and should only be used on websites you have explicit permission to test.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ishanoshada/WooCommerce-Checker.git
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Contribute

Contributions are welcome! Here's how you can get started:

1. Fork the repository.
2. Create a new branch (e.g., `feature-new-feature` or `bug-fix-issue`).
3. Make your changes.
4. Commit your changes and push to your forked repository.
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

