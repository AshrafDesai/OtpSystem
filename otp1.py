from flask import Flask, render_template, request, redirect, url_for, flash
from twilio.rest import Client
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

account_sid = "your_Secret_key"
auth_token = "your_Secret_key"
verify_sid = "your_Secret_key"

client = Client(account_sid, auth_token)

class OTPForm(FlaskForm):
    otp_code = StringField('Enter OTP', validators=[DataRequired()])
    submit = SubmitField('Verify OTP')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        try:
            verification = client.verify.services(verify_sid) \
                .verifications \
                .create(to=phone_number, channel="sms")
            print(verification.status)
            flash("OTP sent successfully", 'success')
            return redirect(url_for('verify_otp', phone_number=phone_number))
        except Exception as e:
            print(f"Error sending OTP: {e}")
            flash("Error sending OTP. Please try again.", 'error')

    return render_template('index.html')

@app.route('/verify_otp/<phone_number>', methods=['GET', 'POST'])
def verify_otp(phone_number):
    form = OTPForm()

    if form.validate_on_submit():
        otp_code = form.otp_code.data
        try:
            verification_check = client.verify.services(verify_sid) \
                .verification_checks \
                .create(to=phone_number, code=otp_code)

            if verification_check.status == 'approved':
                flash("OTP verification successful!", 'success')
            else:
                flash("Invalid OTP. Please try again.", 'error')
        except Exception as e:
            print(f"Error verifying OTP: {e}")
            flash("Error verifying OTP. Please try again.", 'error')

    return render_template('verify_otp.html', form=form, phone_number=phone_number)

if __name__ == '__main__':
    app.run(debug=True,port=2000)
