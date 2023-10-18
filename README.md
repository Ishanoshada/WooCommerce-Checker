WooCommerce Checker is a Python script designed to check if WooCommerce is installed on WordPress websites. It uses the `requests` library for making HTTP requests and provides a simple command-line interface for input.

## Features
- Automatically checks multiple WordPress login URLs with corresponding usernames and passwords.
- Logs successful logins and WooCommerce installations for further analysis.
- Utilizes multiprocessing for concurrent URL checking.

## Usage
1. Create a text file containing WordPress login URLs along with usernames and passwords, separated by '|'.
2. Run the script and provide the path to the input file.
3. The script will attempt to log in and check for WooCommerce installations.

## Requirements
- Python 3.x
- requests library
- colorama library

## Usage Example
```bash
python woocommerce_checker.py logins.txt
