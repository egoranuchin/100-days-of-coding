# file = open("my_file.txt")
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
# file.close()

# delete everything in file and replace it with a new text:
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# add text to the existing:
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# create new file:
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")