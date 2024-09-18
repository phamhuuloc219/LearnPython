import random

def generate_otp():
    # Tạo ngẫu nhiên OTP 6 chữ số
    otp = str(random.randint(100000, 999999))
    print(f"Your OTP is: {otp}")

def main():
    print("OTP Generation Application")
    print("Generating OTP...")
    generate_otp()

if __name__ == "__main__":
    main()