source_file_name = input("Enter the name of the source file: ")
target_file_name = input("Enter the name of the target file: ")

with open(source_file_name, 'r') as source_file, open(target_file_name, 'w') as target_file:
    contents = source_file.read()
    target_file.write(contents)

print("File contents copied successfully.")
