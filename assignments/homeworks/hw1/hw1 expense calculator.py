
"""
Personal Finance Calculator
Student: [Chaiphan Khamphan]
student ID: [6730202114]
Date: [27/7/2025]
Purpose: Calculate monthly budget and savings
"""

monthly_income=float(input("User's monthly income in THB : "))# เงินเดือน รายได้ต่อเดือน
rent_cost = float(input("Monthly rent/housing cost :"))#ต่าเช่า ค่าที่พัก
food_budget=int(input("Monthly food budget in THB :")) #ค่าอาหาร
transportation_cost =float(input("Monthly transportation expenses :"))#ค่าเดินทาง
entertainment_budget = int(input("Monthly entertainment budget :")) #ค่าพักผ่อน,เที่ยว
emergency_fund_percent = float(input("Percentage to save for emergency :"))#  %ของเงินทุนฉุกเฉิน 
investment_percent =float(input("Percentage to invest :"))#   %ของเงินทุนสำหรับการลงทุน


#คำนวณค่าใช้จ่ายต่างๆก่อนนำไปแสดงผล

total_fixed_expenses = rent_cost + transportation_cost                                 #ค่าคงที่ที่ต้องจ่ายแต่ละเดือน
total_variable_expenses = food_budget + entertainment_budget                            #ค่าใช้จ่ายไม่คงที่
total_expenses = total_fixed_expenses + total_variable_expenses                         #ค่าใช้จ่ายทั้งหมด
remaining_income = monthly_income - total_expenses                                      #รายได้คงเหลือ 
emergency_fund_amount =  monthly_income * (emergency_fund_percent / 100)                #เงินฉุกเฉิน  รายรับx %เงินสำหรับฉุกเฉิน/100
investment_amount =  monthly_income * (investment_percent / 100)                        #เงินลงทุน   รายรับx %การลงทุน/100         
available_for_Savings = remaining_income - emergency_fund_amount - investment_amount    #เงินเหลือสำหรับออม เงินที่เหลือ-เงินฉุกเฉิน-เงินลงทน
Expense_Ratio = (total_expenses / monthly_income) * 100                                 #สัดส่วนค่าใช้จ่ายต่อรายได้

#แสดงออกข้อมูลออกทางหน้าจอ
print("=== Personal Finance Calculator ===\nStudent: [Chaiphan Khamphan]\nstudent ID: [6730202114]\nDate: [27/7/2025]\nPurpose: Calculate monthly budget and savings")
print("=== MONTHLY BUDGET REPORT ===") # ใช้print(f" {:,.2f}")เพื่อให้ง่ายต่อการนับเลข
print(f"Income: {monthly_income:,.2f} THB") #แสดงรายรับ
print(f"Fixed Expenses: {total_fixed_expenses:,.2f}THB")#แสดงค่าใช้จ่ายที่มั่นคง
print(f"Variable Expenses: {total_variable_expenses:,.2f} THB")#ค่าใช้จ่ายไม่คงที่
print(f"Total Expenses: {total_expenses:,.2f} THB")
print(f"Remaining: {remaining_income:,.2f} THB\n")

print(f"=== SAVINGS BREAKDOWN ===")
print(f"Emergency_Fund({emergency_fund_percent}%): {emergency_fund_amount:,.2f} THB ")
print(f"Investment ({investment_percent}%): {investment_amount:,.2f} THB")
print(f"Available for Savings: {available_for_Savings:,.2f} THB\n")
if available_for_Savings < 0: #เป็นการเช็คว่าเงินสำหรับออมติดลบหรือไม่ ถ้าติดลบจะแสดงข้อความเตือน
    print(" =======Warning:Save your money Sirrr=======")
print(f"=== ANALYSIS ===")
print(f"Expense Ratio: {Expense_Ratio:,.2f}%")
