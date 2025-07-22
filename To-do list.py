Tasks=[]
while True:
    print("1:Add Task")
    print("2:Delete Task")
    print("3:View Task")
    print("4:Edit Task")
    print("5:Exit")

    try:
        choice=int(input("Enter Your Choice: "))
    except ValueError:
        print("please enter correct choices only\n")
        continue
           
    if choice==1:
            addtask=input("enter Your adding Task:")
            if addtask in Tasks:
                print("this task already there in the list\n")
            else:
                Tasks.append(addtask)
                print("Tasks added \n")

    elif choice==2:
        removetask=input("enter your removing task:")
        if removetask in Tasks:
                Tasks.remove(removetask)
                print(f"you removed {removetask}\nnow awailable tasks {Tasks} \n ")
        else:
                print(f"{removetask} is not there in tasks list\n")     

    elif choice==3:
            print(f"{Tasks} \n ")
            
    elif choice==4:
        taskname=input("enter your try to updated taskname: ")
        if taskname in Tasks:
            updatedtask=input("enter your new updated task: ")
            Tasks[Tasks.index(taskname)]=updatedtask
            print(f"your updatedtask is {updatedtask}")
        else:
            print(f"this task {taskname} is not there in the list please enter correct task \n")
        
        
    elif choice==5:
            break
    else:
            print("enter valid choice only")