

def mail_user(streaks,subject,body) :
    from config.env_variables import sender_email,receiver_email,app_password
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Use 465 for SSL, 587 for TLS
    # Set up the MIME format for the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    # Send the email using SMTP
    try:
        # Connect to the Gmail SMTP server using TLS
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection using TLS
            server.login(sender_email, app_password)  # Use app password for login
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")