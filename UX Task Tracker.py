# Import necessary modules
import datetime # Importing the datetime module

# Define styles for text formatting
def green(text):
    return f"\033[92m{text}\033[00m" # ANSI escape code for green text

def red(text):
    return f"\033[91m{text}\033[00m" # ANSI escape code for red text

def gold(text):
    return f"\033[93m{text}\033[00m" # ANSI escape code for yellow text

def print_bold(text):
    return("\033[1m" + text + "\033[0m") # ANSI escape code for bold text

# Define the main function
def main():
    # Welcome message
    print(f"🚀 Welcome to the UX Task Analysis Tracker 🚀")
    print() # Print a blank line for spacing

    # Step 1: Define the project name
    project_name = input("📝 Enter the name of your project: ") # Prompt user for project name
    print() # Print a blank line for spacing

    # Step 2: Define the project type
    project_type = "" # Initialize project_type variable
    
    # Loop until a valid choice is made
    while project_type not in ['1', '2']: # Prompt user for project type
        print("📂 Choose the project type:")
        print(" 1. Developing a brand-new product")
        print(" 2. Updating an existing system")
        project_type = input("Enter your choice (1 or 2): ") # Check for invalid input
        if project_type not in ['1', '2']:
            print(red("Invalid choice. Please try again.")) # Print error message in red
    
    # Set project_type based on user input
    project_type = "Brand-new Product" if project_type == '1' else "Updating Existing System"
    print() # Print a blank line for spacing

    # Initialize storage for tasks and their details
    tasks = [] # List to hold all tasks

    # Step 3-5: Input tasks, sub-tasks, and steps
    while True: # Loop to allow multiple tasks to be added
        print("🛠️ Define a user goal/task:")
        task_name = input("💡 Enter the user goal (e.g., Purchase jeans): ") # Prompt for task name

        # Add sub-tasks and steps for the task
        sub_tasks = [] # List to hold sub-tasks for the current task
        while True: # Loop to add sub-tasks
            print(f"📋 Adding sub-tasks for the task: {task_name}")
            sub_task_name = input("🔹 Enter sub-task name (or type 'done' to finish adding sub-tasks): ")
            if sub_task_name.lower() == "done": # Check if user is done adding sub-tasks
                break
            
            # Add steps for the sub-task
            steps = [] # List to hold steps for the current sub-task
            while True: # Loop to add steps
                print(f"📂 Adding steps for sub-task: {sub_task_name}")
                step_description = input("   🔸 Enter step description (or type 'done' to finish adding steps): ") # Check if user is done adding steps
                if step_description.lower() == "done":
                    break
                steps.append(step_description) # Add step description to steps list
            
            # Append the sub-task with its steps to the sub_tasks list
            sub_tasks.append({
                "sub_task_name": sub_task_name,
                "steps": steps
            })

        # Store the task and its sub-tasks in the tasks list
        tasks.append({
            "task_name": task_name,
            "sub_tasks": sub_tasks
        })

        # Check if the user wants to add another task
        add_another_task = input(gold("Do you want to add another task? (yes/no): ")).lower()
        if add_another_task != "yes": # Exit loop if user does not want to add another task
            break

    # Step 6: Input additional details for each task
    for task in tasks: # Iterate over each task
        print(f"\n⏳ Additional details for task: {task['task_name']}")
        
        # Input time taken
        while True: # Loop until valid time is entered
            try:
                time_taken = float(input("⏱️ Enter time taken to finish the task (in seconds): "))
                break  # Exit the loop if input is valid
            except ValueError:
                print(red("❌ Invalid input. Please enter a valid number for time taken to finish the task (in seconds)."))

        # Input mental process
        while True:
            print("🧠 Choose the mental process type for this sub-task:")
            print(" 1. Cognitive")
            print(" 2. Judgement")
            print(" 3. Decision")
            mental_process = input("Enter your choice (1, 2, or 3): ")
        
            if mental_process in ['1', '2', '3']:
                mental_process = {
                    '1': "Cognitive",
                    '2': "Judgement",
                    '3': "Decision"
                }[mental_process]
                break  # Exit the loop if input is valid
            else:
                print(red("❌ Invalid input. Please enter 1, 2, or 3."))

        # Input physical requirement
        while True:
            physical_requirement = input("🤸 Enter any physical requirement (or type 'none' if none): ")
            if physical_requirement.lower() == "none":
                physical_requirement = "None"
                break
            else:
                break

        # Store additional details in the task
        task["time_taken"] = time_taken
        task["mental_process"] = mental_process
        task["physical_requirement"] = physical_requirement

    # Step 7: Display the results
    print("\n🎉 Results:")
    total_time = 0
    total_steps = 0

    for task in tasks:
        print(f"\n📌 Task: {task['task_name']}")
        print(f"   ⏱️ Time Taken: {task['time_taken']} seconds")
        print(f"   🧠 Mental Process: {task['mental_process']}")
        print(f"   🤸 Physical Requirement: {task['physical_requirement']}")
        total_time += task["time_taken"]

        for sub_task in task["sub_tasks"]:
            print(f"   🔹 Sub-task: {sub_task['sub_task_name']}")
            for step in sub_task["steps"]:
                print(f"     🔸 Step: {step}")
                total_steps += 1

    print(f"\n{green(f'Total Time: {total_time} seconds')}")
    print(f"{green(f'Total Number of Steps: {total_steps}')}")

    print("\nThank you for using the UX Task Analysis Tracker!")

# Run the application
if __name__ == "__main__":
    main()