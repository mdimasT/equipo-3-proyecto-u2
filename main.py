import stack, linked_list, ds_queue
menu_control = True
def main_menu():
    global menu_control
    
    print("Menu")
    print("")
    print("Choose an option")
    print("1.-Queue")
    print("2.-Stack")
    print("3.-Linked list")
    print("4.-Exit")
 
    option = input()
    if option.upper() == "QUEUE" or option == "1":
        queue_menu()

    elif option.upper() == "STACK" or option == "2":
        stack_menu()

    elif option.upper() == "LINKED LIST" or option == "3":
        linked_list_menu()

    elif option.upper() == "EXIT" or option == "4":
        menu_control = False

myqueue = ds_queue.Queue()
mystack = stack.Stack()
myLinkedList = linked_list.LinkedList()

def queue_menu():
    
    print("Options")
    print("")
    print("1.-Insert data (Enqueue)")
    print("2.-Delete the last number (Dequeue)")
    print("3.-Show the number on top (Peek)")
    print("4.-Return")

    options_qs = input()

    if options_qs == "1":
        print("Insert five numbers")
        i = 1
        while i <= 5:
            print("Insert the ",i, "number")
            qs_number = input()
            myqueue.enqueue(qs_number)
            i = i + 1
        print("The numbers have been added succesfuly")
        queue_menu()

    elif options_qs == "2":
       print(myqueue.dequeue(),"was deleted: ")
       queue_menu()

    elif options_qs == "3":
       print(myqueue.peek())
       queue_menu()

    elif options_qs == "4":
        main_menu()

    else:
        print("Inavalid option")
        queue_menu()


    
    
while menu_control:
     main_menu()
    

 