# WhatsApp Message Automation

A Python script that automates sending WhatsApp messages to multiple contacts using Selenium WebDriver.

## Features

- Send automated messages to multiple WhatsApp contacts
- Read contacts from a text file
- Read message content from a text file
- Automatic retry every 10 minutes
- Chrome profile support to maintain WhatsApp Web session

## Prerequisites

- Python 3.x
- Google Chrome Browser
- ChromeDriver
- WhatsApp Web account

## Required Python Packages

bash
pip install selenium

## Project Structure

├── automation.py
├── contacts.txt
├── message.txt
└── README.md


## Setup Instructions

1. Create a Chrome profile for WhatsApp automation:
   - Navigate to `C:\Users\[YourUsername]\AppData\Local\Google\Chrome\User Data\`
   - Create a new folder named `WatsappAutomation`

2. Prepare your contact list:
   - Create a `contacts.txt` file
   - Add one contact name per line
   - Example:
     ```
     Anas
     Baba
     ather
     ```

3. Prepare your message:
   - Create a `message.txt` file
   - Write the message you want to send
   - The message can be multiple lines

## Usage

1. Run the script:

bash
python automation.py


2. The script will:
   - Open WhatsApp Web in Chrome
   - Wait for you to scan the QR code (first time only)
   - Send the message to each contact in the contacts list
   - Retry every 10 minutes

## Important Notes

- Make sure your WhatsApp Web is logged in
- Contact names must exactly match as they appear in your WhatsApp contacts
- The script uses XPath selectors which may need updates if WhatsApp Web's interface changes
- Keep your system active while the script is running
- Ensure good internet connectivity

## Error Handling

The script includes basic error handling:
- Prints error messages if unable to send to specific contacts
- Continues to next contact if one fails
- Automatically retries every 10 minutes

## Limitations

- Requires Chrome browser
- Needs active internet connection
- WhatsApp Web must be accessible
- Contact names must be exact matches

## Disclaimer

This script is for educational purposes only. Use it responsibly and in accordance with WhatsApp's terms of service. Automated messaging may be against WhatsApp's policies in certain contexts.

## License

This project is open source and available under the MIT License.

