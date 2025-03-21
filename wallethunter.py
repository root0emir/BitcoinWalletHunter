import os
import ecdsa
import hashlib
import base58
import bitcoin
import threading
import time
import csv
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

keep_running = True
count = 0

def generate_private_key():
    return os.urandom(32)

def private_key_to_wif(private_key):
    extended_key = b"\x80" + private_key
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    return base58.b58encode(extended_key + checksum)

def private_key_to_public_key(private_key):
    signing_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    verifying_key = signing_key.get_verifying_key()
    return bytes.fromhex("04") + verifying_key.to_string()

def save_wif(wif):
    with open('log.txt', 'a') as f:
        f.write("\n")
        f.write(wif)

def count_found():
    global count
    count += 1

# Check the balance from the database
def check_balance():
    private_key = generate_private_key()
    wif_private_key = private_key_to_wif(private_key).decode()
    public_key = private_key_to_public_key(private_key).hex()
    address = bitcoin.pubkey_to_address(public_key)

    try:
        with open('blockchair_bitcoin_addresses_latest.tsv', 'r') as file:
            tsv_reader = csv.reader(file, delimiter='\t')
            for row in tsv_reader:
                if row[0] == address:
                    final_balance = float(row[1])
                    if final_balance != 0:
                        count_found()
                        with open('FoundAddress.txt', 'a') as f:
                            f.write("\n" + wif_private_key)
                            print("root0emir")
                    print("WIF Private Key:", wif_private_key)
                    print("Public Key:", public_key)
                    print("Address:", address)
                    print("Balance:", final_balance)
                    print("---------------------")
                    print("\n", "Found Wallet with Balance:", count, "\n")
                    save_wif(wif_private_key)
                    return
            print(Fore.RED + "Address not found in the database.")
    except FileNotFoundError:
        print(Fore.RED + "Error: The database file 'blockchair_bitcoin_addresses_latest.tsv' was not found. Please make sure the file is in the same directory as this script.")
    except Exception as e:
        print(Fore.RED + "Error: An unexpected error occurred. Please check your file and try again.")
        print(e)

def start_hunting():
    while keep_running:
        check_balance()
        time.sleep(3)  # Pause for 3 seconds before the next check

def show_guide():
    guide_text = """
================== GUIDE ==================
1. Download the blockchair_bitcoin_addresses_latest.tsv file from:
   https://gz.blockchair.com/bitcoin/addresses/
   
2. Place the file in the same directory as this script.
   
3. Run the script and start hunting for Bitcoin addresses.
=================================================
"""
    print(Fore.GREEN + guide_text)

def menu():
    ascii_art = r"""

DEVELOPED BY

                 _    ___                 _      
 _ __ ___   ___ | |_ / _ \  ___ _ __ ___ (_)_ __ 
| '__/ _ \ / _ \| __| | | |/ _ \ '_ ` _ \| | '__|
| | | (_) | (_) | |_| |_| |  __/ | | | | | | |   
|_|  \___/ \___/ \__|\___/ \___|_| |_| |_|_|_|   
                                                 


⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀
⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠟⠿⠿⡿⠀⢰⣿⠁⢈⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀
⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣤⣄⠀⠀⠀⠈⠉⠀⠸⠿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⢠⣶⣶⣤⡀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⡆
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠼⣿⣿⡿⠃⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢀⣀⣀⠀⠀⠀⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠁⠀⠀⣼⣿⣿⣿⣦⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⡿
⠸⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠛⠛⠿⠟⠋⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠇
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⣤⡄⠀⣀⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣄⣰⣿⠁⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀
⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⢿⣿⣿⣿⣿⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀

"""
    print(Fore.CYAN + ascii_art)
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to BTC Wallet Hunter")
    print(Fore.YELLOW + "---------------------")
    print(Style.BRIGHT + Fore.BLUE + "1. Start BTC Wallet Hunting")
    print(Style.BRIGHT + Fore.BLUE + "2. Settings")
    print(Style.BRIGHT + Fore.BLUE + "3. Guide")
    print(Style.BRIGHT + Fore.BLUE + "4. About")
    print(Style.BRIGHT + Fore.BLUE + "5. Exit")

    while True:
        choice = input(Fore.MAGENTA + "Enter your choice: ")

        if choice == '1':
            start_threads()
        elif choice == '2':
            settings()
        elif choice == '3':
            show_guide()
        elif choice == '4':
            about()
        elif choice == '5':
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

def start_threads():
    global keep_running
    keep_running = True
    threads = []
    for i in range(thread_count):
        t = threading.Thread(target=start_hunting)
        threads.append(t)
        t.start()
    try:
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        keep_running = False
        print("Stopping all threads...")

def settings():
    global thread_count, log_file, found_file
    print("Current settings:")
    print(f"1. Thread Count: {thread_count}")
    print(f"2. Log File: {log_file}")
    print(f"3. Found File: {found_file}")

    choice = input("Enter the number of the setting you want to change (or press enter to go back): ")

    if choice == '1':
        thread_count = int(input("Enter new thread count: "))
    elif choice == '2':
        log_file = input("Enter new log file path: ")
    elif choice == '3':
        found_file = input("Enter new found file path: ")

    print(Fore.GREEN + "Settings updated successfully.")

def about():
    print(Fore.CYAN + "BTC Hunter")
    print(Fore.CYAN + "Version: 1.0")
    print(Fore.CYAN + "Author: root0emir")
    print(Fore.CYAN + "Description: A Bitcoin Wallet Miner, which is a solo project, is written in Python.")

if __name__ == "__main__":
    thread_count = 5  # Number of parallel threads
    log_file = 'log.txt'
    found_file = 'FoundAddress.txt'
    menu()