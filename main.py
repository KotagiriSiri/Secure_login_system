from detection import predict_email

print("📧 Email Spam Detector")

while True:
    user_input = input("Enter email text (or type 'exit'): ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    result = predict_email(user_input)

    if result == "spam":
        print("🚫 This is SPAM")
    else:
        print("✅ This is NOT spam")