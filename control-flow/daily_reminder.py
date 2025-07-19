
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
        priority_text = "high priority"
    case "medium":
        priority_text = "medium priority"
    case "low":
        priority_text = "low priority"

if time_bound == "yes":
    time_msg = " that requires immediate attention today!"
else:
    time_msg = " Consider completing it when you have free time."

print(f"Reminder: '{task}' is a {priority_text} task{time_msg}")
