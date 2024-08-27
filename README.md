Forex Currency Converter -
Overview: 
The Forex Currency Converter is a web application that allows users to convert between different currencies. It fetches real-time exchange rates using the ExchangeRate.host API and calculates conversions based on user input. The application is built using Python, Flask, and HTML.

Features
Real-time currency conversion using ExchangeRate.host API.
User-friendly interface for selecting currencies and inputting amounts.
Support for a wide range of currencies.
Lightweight and easy to deploy.
Technologies Used
Python: The core programming language used to handle backend logic.
Flask: A lightweight WSGI web application framework used to build the server-side of the application.
HTML: For structuring the front-end interface.
ExchangeRate.host API: Provides real-time exchange rate data for various currencies.


Installation
Prerequisites
Python 3.x installed on your system.
Flask installed (can be installed via pip).
An API key from ExchangeRate.host (if applicable).


clone the repository:
git clone https://github.com/manroopSandhu/forexConvertor
cd forexConvertor

Create and Activate a Virtual Environment:
python3 -m venv venv
source venv/bin/activate

Install Dependencies:
pip install -r requirements.txt

Run the Application:
flask run

Usage:
Open your web browser and navigate to http://127.0.0.1:5000/.
Select the currency you wish to convert from and the currency you wish to convert to.
Enter the amount you wish to convert.
Click on the "Convert" button to see the converted amount.

forex-currency-converter/
│
├── app.py               # The main Flask application
├── templates/
│   ├── index.html       # HTML template for the home page
│   └── display.html     # HTML template for displaying conversion results
├── static/
│   └── styles.css       # CSS file for styling
├── test.py              # Unit tests for the application
├── requirements.txt     # List of dependencies
└── README.md            # This file
