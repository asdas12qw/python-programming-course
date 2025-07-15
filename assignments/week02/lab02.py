"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
ways = input("Select menu: 1. THB to USD  2. USD to THB: ")
amount = float(input("Input amount of currency: "))
rate = 35.5

if ways == "1":
    USD = amount / rate
    print(f"{amount} THB / {rate} = {USD:.2f} USD")
    print(f"Amount entered: {amount} THB")
if ways == "2":
    THB = amount * rate
    print(f"{amount} USD * {rate} = {THB:.2f} THB")
    print(f"Amount entered: {amount} USD")

1