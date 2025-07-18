task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority. Please verify."

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if "Reminder" in reminder:
        reminder += "."
    reminder += " Consider completing it when you have free time."

print(reminder)