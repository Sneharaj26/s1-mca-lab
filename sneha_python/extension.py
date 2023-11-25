filename = input("Enter the filename:")
extension = filename.split(".")
print("File extension is : ", extension[-1] if len(extension)>1 else"Unknown extension")