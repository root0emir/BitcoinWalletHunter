# BitcoinWalletHunter

# Bitcoin Wallet Hunter

BTC Wallet Hunter is a Bitcoin wallet miner that checks balances from a database of Bitcoin addresses. This tool generates private keys, converts them to public keys and addresses, and checks for balances in the provided database file.

## Features

- Generates private keys and corresponding public keys.
- Converts private keys to Wallet Import Format (WIF).
- Checks Bitcoin addresses against a local database file for balances.
- Logs found addresses and private keys to files.
- Multi-threaded support for faster processing.
- User-friendly menu for easy navigation.

## Requirements

- Python 3.x
- Required Python packages:
  - `ecdsa`
  - `base58`
  - `requests`
  - `bitcoin`
  - `colorama`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/root0emir/BitcoinWalletHunter.git
    cd btc-hunter
    ```

2. Install the required Python packages:
    ```sh
    pip install ecdsa base58 requests bitcoin colorama
    ```

3. Download the latest Bitcoin addresses database file from [Blockchair](https://gz.blockchair.com/bitcoin/addresses/):
    - Place the downloaded `blockchair_bitcoin_addresses_latest.tsv` file in the same directory as the script.

## Usage

Run the script:
```sh
python main.py
```

Follow the on-screen menu to start BTC hunting, configure settings, view the guide, or learn more about the tool.

### Menu Options

1. **Start BTC Hunting**: Starts the process of generating and checking Bitcoin addresses.
2. **Settings**: Configure the number of threads, log file path, and found file path.
3. **Guide**: Provides instructions on how to download and place the database file.
4. **About**: Information about the tool and its author.
5. **Exit**: Exit the application.

### Guide

1. Download the `blockchair_bitcoin_addresses_latest.tsv` file from [Blockchair](https://gz.blockchair.com/bitcoin/addresses/).
2. Place the file in the same directory as this script.
3. Run the script and start hunting for Bitcoin addresses.

### Settings

You can configure the following settings:
- **Thread Count**: Number of parallel threads for checking addresses.
- **Log File**: Path to the log file where private keys are saved.
- **Found File**: Path to the file where found addresses with balances are saved.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- **root0emir**

developed by root0emir
