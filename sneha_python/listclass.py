class ListManager:
    def __init__(self):
        self.my_list = []

    def add_element(self, element):
        self.my_list.append(element)
        print(f"Element '{element}' added to the list.")

    def delete_element(self, element):
        if element in self.my_list:
            self.my_list.remove(element)
            print(f"Element '{element}' deleted from the list.")
        else:
            print(f"Element '{element}' not found in the list.")

    def display_elements(self):
        if not self.my_list:
            print("The list is empty.")
        else:
            print("Elements in the list:")
            for element in self.my_list:
                print(element)

# Example usage:
list_manager = ListManager()

while True:
    print("\nMenu:")
    print("1. Add element")
    print("2. Delete element")
    print("3. Display elements")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        element = input("Enter the element to add: ")
        list_manager.add_element(element)
    elif choice == "2":
        element = input("Enter the element to delete: ")
        list_manager.delete_element(element)
    elif choice == "3":
        list_manager.display_elements()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
