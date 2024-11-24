# Taiko Slow Parser

A Python script for scraping point balances from user profiles on the **[Trailblazers Taiko website](https://trailblazers.taiko.xyz)**. The script leverages Selenium and BeautifulSoup to handle dynamic content loading.

## Features

- Parse point balances for multiple user addresses.
- Support for address lists stored in a text file.
- Automatically waits for JavaScript-rendered content to load.

## Requirements

- Python 3.7+
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/taiko-slow-parser.git
   cd taiko-slow-parser
2. Install the required Python libraries:
 ```bash
   pip install -r requirements.txt
```
3. Ensure you have ChromeDriver installed and accessible:

  Download ChromeDriver matching your Chrome version.
  Place it in a directory included in your system's PATH, or specify its location in the script.

Usage
1. Prepare a file named addresses.txt in the same directory as the script. Each line should contain one user address

2. Run the script:

 ```bash
   python main.py
```
The script will output the results in the format:
```bash
0x0DaefA9d9DE5fF506b8d340F75EAB8865a71a327 - 60,474.90
0x1234567890abcdef1234567890abcdef12345678 - 12,345.67
0xaBcDEF1234567890ABCDEF1234567890abcdef12 - Element not found
```

The method is not the fastest or most convenient, but it works!


