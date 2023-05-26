def grocery_list():
    # empty container to store groceries
    # value is declared here so that it is not reset to an empty list every time the loop runs
    groceries = []

    while True:
        # list of options for user to choose from
        print("\n===== Grocery List =====")
        print("1. Add Item")
        print("2. View Items")
        print("3. Delete Item")
        print("4. Exit")

        # ask user for choice
        choice = input("Enter your choice: ")

        # handle user's choice
        # if 1 is selected, user is prompted to "Enter the food: ", and that food is added (append) to the list
        # print "Food added successfully!"
        if choice == "1":
            grocery = input("Enter the food: ")
            groceries.append(grocery)
            print("Food added successfully!")

        # if 2 is selected, print "Here is your list:" and then print each item in the list
        elif choice == "2":
            print("Here is your list:")
            # enumerate() function iterates a count for each item in the groceries array; start=1 starts the count at 1 instead of 0
            for index, grocery in enumerate(groceries, start=1):
                print(f"{index}. {grocery}")
        # if 3 is selected, print "No groceries to delete." if the list is empty
        elif choice == "3":
            if len(groceries) == 0:
                print("No groceries to delete.")
            # otherwise, prompt the user to "Enter the grocery index to delete: "
            else:
                # int function converts the user's input to an integer, and subtracts 1 to get the 'real' index of the grocery to delete
                index = int(input("Enter the grocery index to delete: ")) - 1
                if index >= 0 and index < len(groceries):
                    # pop() function removes the item at the specified index
                    deleted_grocery = groceries.pop(index)
                    # print the deleted grocery
                    print(f"'{deleted_grocery}' deleted successfully!")
                # if the index is invalid, print "Invalid grocery index."
                else:
                    print("Invalid grocery index.")
        # if 4 is selected, print "Goodbye!" and break out of the loop
        elif choice == "4":
            print("Goodbye!")
            break
        # if the user enters anything other than 1, 2, 3 or 4, print "Invalid choice. Please try again."
        else:
            print("Invalid choice. Please try again.")

# call the function
grocery_list()