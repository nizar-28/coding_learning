# Ask user age and give advice

age = int(input("What is your age? "))

if age < 18:
    print("You are young. Study hard!")
elif age <30:
    print("You are young adult. Chase your dreams!")
else:
    print("Age is just a number. Keep going!")

times = int(input("How many times should I cheer for you? "))
for i in range(times):
    print("You can do it! ファイトです！")