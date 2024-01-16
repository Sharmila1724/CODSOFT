tasks = []
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully.")
def view_tasks():
    if len(tasks) == 0:
        print("There is no task to view.")
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}.{task}")    
def delete_task():   
    if len(tasks) == 0:
        print("There is no task to delete")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        option = int(input("Enter the task num to be deleted:"))
        if 0 < option <=len(tasks):
            del tasks[option-1]
            print("The task is deleted successfully. ")
        else:
            print("Invalid")
          
def main():
    while True:
        print("\n===== TO-Do-List =====")
        print("1.Add Your Task:")
        print("2.View Your Task:")
        print("3.Delete Your Task:")
        print("4.Exit")

        option=int(input("Enter your option:"))
        if option==1:
            add_task()
        elif option==2:
            view_tasks()
        elif option==3:
            delete_task()
        elif option==4:
            print("Thank you for using this application.")
            break
        else:
            print("Invalid option.. Try again...")            
if __name__ == "__main__" :
    main()  
