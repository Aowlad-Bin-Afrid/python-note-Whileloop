# while_loop_note.py
# Created by ChatGPT
# Date: 2025-10-31
# Description: examples of Python while loop

# ---------------------------------------------------------
# 🎯 Purpose:
# This file explains everything about the Python "while loop":
# - basic structure
# - condition checking
# - break, continue, else
# - nested loops
# - infinite loop
# - user input example
# - using while loop for number, list, string
# ---------------------------------------------------------


# 🟩 1️⃣ Basic while loop — print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1
# Explanation:
# while i <= 10 → loop চলবে যতক্ষণ i এর মান 10 বা তার কম থাকে
# i += 1 → প্রতিবার ১ করে বাড়ে
# ---------------------------------------------------------


# 🟦 2️⃣ while loop with step value (even numbers)
i = 2
while i <= 10:
    print("Even number:", i)
    i += 2
# ---------------------------------------------------------


# 🟨 3️⃣ Reverse loop
i = 10
while i > 0:
    print("Reverse:", i)
    i -= 1
# ---------------------------------------------------------


# 🟧 4️⃣ Using if condition inside while loop
i = 1
while i <= 5:
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
    i += 1
# ---------------------------------------------------------


# 🟥 5️⃣ Using break — stop the loop early
i = 1
while i <= 10:
    if i == 5:
        print("Loop stopped at", i)
        break
    print("Number:", i)
    i += 1
# break → stops the loop immediately
# ---------------------------------------------------------


# 🟪 6️⃣ Using continue — skip a specific step
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("Value:", i)
# continue → skips current iteration
# ---------------------------------------------------------


# 🟫 7️⃣ Using else with while loop
i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("Loop finished successfully!")
# else → runs only if loop ends normally (no break)
# ---------------------------------------------------------


# ⬛ 8️⃣ Nested while loop — loop inside another loop
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1
# ---------------------------------------------------------


# 🟨 9️⃣ Calculate the sum of numbers
total = 0
i = 1
while i <= 5:
    total += i
    i += 1
print("Sum from 1 to 5:", total)
# ---------------------------------------------------------


# 🟩 🔟 While loop with list
fruits = ["apple", "banana", "mango"]
i = 0
while i < len(fruits):
    print("Fruit:", fruits[i])
    i += 1
# ---------------------------------------------------------


# 🟦 1️⃣1️⃣ Infinite loop (⚠️ Example only, use carefully!)
# This will run forever unless manually stopped
# Uncomment to test (⚠️ Warning: runs infinitely!)
# while True:
#     print("This loop runs forever! Press Ctrl+C to stop.")
# ---------------------------------------------------------


# 🟧 1️⃣2️⃣ User input with while loop
# This loop will keep asking until correct input is given
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted!")
# ---------------------------------------------------------


# ✅ Summary:
# ---------------------------------------------------------
# 🔹 while loop — used when you don't know exactly how many times to iterate
# 🔹 condition — loop runs while condition is True
# 🔹 break — stops the loop immediately
# 🔹 continue — skips one iteration
# 🔹 else — runs when the loop finishes without break
# 🔹 nested loop — loop inside another loop
# 🔹 infinite loop — runs forever until manually stopped
# 🔹 user input — useful for validation and repetition
# ---------------------------------------------------------
