import tkinter as tk
from twilio.rest import Client

class OTPVerificationGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("OTP Verification")

        self.label = tk.Label(master, text="Enter your phone number:")
        self.label.pack(pady=10)

        self.phone_entry = tk.Entry(master)
        self.phone_entry.pack(pady=10)

        self.send_otp_button = tk.Button(master, text="Send OTP", command=self.send_otp)
        self.send_otp_button.pack(pady=10)

        self.otp_label = tk.Label(master, text="Enter OTP:")
        self.otp_label.pack(pady=10)

        self.otp_entry = tk.Entry(master)
        self.otp_entry.pack(pady=10)

        self.verify_otp_button = tk.Button(master, text="Verify OTP", command=self.verify_otp)
        self.verify_otp_button.pack(pady=10)

    def send_otp(self):
        phone_number = self.phone_entry.get()
        if phone_number:
            try:
                verification = client.verify.v2.services(verify_sid) \
                    .verifications \
                    .create(to=phone_number, channel="sms")
                print(verification.status)
            except Exception as e:
                print(f"Error sending OTP: {e}")
        else:
            print("Please enter a valid phone number.")

    def verify_otp(self):
        phone_number = self.phone_entry.get()
        otp_code = self.otp_entry.get()

        if phone_number and otp_code:
            try:
                verification_check = client.verify.v2.services(verify_sid) \
                    .verification_checks \
                    .create(to=phone_number, code=otp_code)
                print(verification_check.status)
            except Exception as e:
                print(f"Error verifying OTP: {e}")
        else:
            print("Please enter both phone number and OTP.")

if __name__ == "__main__":
    account_sid = "ACf76159925fca875edf27f8e3d700ba3c"
    auth_token = "baece64ca7fe44edce367ff31aa63216"
    verify_sid = "VA7437369f46aa2db48682f976620a0a18"
    verified_number = "+919967452141"

    client = Client(account_sid, auth_token)

    root = tk.Tk()
    app = OTPVerificationGUI(root)
    root.mainloop()
