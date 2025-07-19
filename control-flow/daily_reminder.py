task = input("Enter your task: ")

allowed_priorities = {"high", "medium", "low"}
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in allowed_priorities:
        break
    print("Please enter exactly 'high', 'medium', or 'low'.")

while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in {"yes", "no"}:
        break
    print("Please answer 'yes' or 'no'.")

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
   
    reminder += " Consider completing it when you have free time."

print(reminder)
