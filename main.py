
tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the list")


def listTasks():
    if not tasks:
         print("There are no task currently ")
    else:
        print("Here are all current tasks: ")
        for index in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # you want to delete: "))
        if taskToDelete >= 0 and  taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been succesfully deleted")
        
        else:
             print(f"Task #{taskToDelete} is not found")
    except:
        print("invalid input")


if __name__ == "__main__":
    print ("Welcome to my todo list app")

    while True:
        print("\n")
        print("Select one of the options")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
 
        choice = input("Enter your choice ")

        if (choice == "1"):
            addTask()


        elif (choice == "2"):
            deleteTask()

        elif(choice == "3"):
            listTasks()

        elif(choice == "4"):
            break

        else:
            print("Invalid input")

    print("Goodbye")
