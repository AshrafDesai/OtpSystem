# Flask Twilio OTP Verification

This is a simple Flask web application that demonstrates OTP (One-Time Password) verification using Twilio.

## Features

- Sends OTP to a provided phone number via Twilio.
- Verifies the entered OTP.

## Prerequisites

Before running the application, make sure you have the following:

- [Python](https://www.python.org/) installed.
- Twilio account SID, auth token, and a Twilio Verify service SID.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/AshrafDesai/flask-twilio-otp-verification.git
    ```

2. Update the configuration:

    - Open `app.py` and replace the placeholder values for `account_sid`, `auth_token`, and `verify_sid` with your Twilio credentials.

3. Run the application:

    ```bash
    python app.py
    ```

4. Access the application in your browser:

    Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to send OTP.

## Usage

1. Open the application in your browser.
2. Enter the phone number and click "Send OTP".
3. Check the console for OTP status.
4. Enter the received OTP on the verification page.

## Troubleshooting

- If you encounter issues with sending or verifying OTPs, check the Twilio Console for error messages.
- Ensure your Twilio account has sufficient balance or credits.

## Notes

- This application is for educational purposes and may require improvements for production use.


