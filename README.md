# Top Stories Emailer

The Top Stories Emailer is a Python script that automatically scrapes the top headlines from multiple sources and sends them to your email address. It aggregates the latest news from CoinDesk, The New York Times (Business section), and the Financial Times (Crypto & Finance section) to provide you with a comprehensive overview of the top stories in the cryptocurrency and finance domains.

## Features

- Scrapes the top headlines from CoinDesk, The New York Times (Business), and the Financial Times (Crypto & Finance).
- Sends the aggregated headlines via email to the specified recipient (your email address).
- Scheduled to run automatically at 8:00 AM daily using the `schedule` library.
- Utilizes BeautifulSoup for web scraping and smtplib for email sending.

## Getting Started

### Prerequisites

- Python 3.x
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- `schedule` library (`pip install schedule`)

### Installation

1. Clone the repository:

2. Install dependencies:

### Configuration

1. Open `main.py` in a text editor.

2. Replace `"your_email@gmail.com"` with your email address in the `my_email` variable.

3. Replace `"your_password"` with your email password in the `server.login` function (ensure that you handle sensitive information securely).

### Usage

1. Run the script:

2. Check your email inbox for the latest top headlines from CoinDesk, The New York Times, and the Financial Times.

3. Optionally, customize the sources, schedule, or email content according to your preferences by modifying the `send_email` and `Top_Stories` functions in `main.py`.

## Contributing

Contributions to the project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

