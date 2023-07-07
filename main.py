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


def stack_menu():
    
    print("Options")
    print("")
    print("1.-Insert data (push)")
    print("2.-Delete last number (pop)")
    print("3.-Show the number on top (Peek)")
    print("4.-Return")

    options_s = input()

    if options_s == "1":
        print("Insert five numbers")
        i = 1
        while i <= 5:
            print("Insert the ",i, "number")
            s_number = input()
            mystack.push(s_number)
            i = i + 1
        print("The numbers have been added succesfuly")
        stack_menu()

    elif options_s == "2":
       print(mystack.pop(),"was deleted: ")
       stack_menu()

    elif options_s == "3":
       print(mystack.peek())
       stack_menu()

    elif options_s == "4":
        main_menu()

    else:
        print("Inavalid option")
        stack_menu()


def linked_list_menu():
    
    print("Options")
    print("")
    print("1.-Insert data at beggining")
    print("2.-Insert data at end")
    print("3.-Insert data after node")
    print("4.-Delete node")
    print("5.-Show the list")
    print("6.-Return")

    options_l = input()

    if options_l == "1":
        print("Insert the number at the beggining")
        Lnumber = int(input()) 
        myLinkedList.insert_at_beginning(Lnumber)
        
        print("The number has been added succesfuly")
        linked_list_menu()

    elif options_l == "2":
        print("Insert the number at the end")
        Lnumber = int(input()) 
        myLinkedList.insert_at_end(Lnumber)
        print("The number has been added succesfuly")
        linked_list_menu()


    elif options_l == "3":
       print("Insert after node")
       print("After what node would you like to add the number?")
       node = int(input())

       print("What number would you like to add?")
       Lnumber = input()

       myLinkedList.insert_after_node(node, Lnumber)
       print("The number has been added succesfuly")
       linked_list_menu()


    elif options_l == "4":
        print("Delete node")
        print("What node would you like to delete?") 
        node = int(input())
        myLinkedList.delete_node(node)
        print("The node has been deleted")
        linked_list_menu()


    elif options_l == "5":
        print("Show the  linked list")
        myLinkedList.display()
        linked_list_menu()

    elif options_l == "6":
        main_menu()
        

    else:
        print("Inavalid option")
        linked_list_menu()
    
    
while menu_control:
     main_menu()
    

 