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

    
while menu_control:
     main_menu()
    

 