#created a text file and write data into it
with open("sample.txt","w") as f:
    f.write("Hello World\n")
    f.write("New line.\n")
print("file created and text written")

#read and display the file
with open("sample.txt","r") as f:
    content = f.read()
    print(content)

#append data to file
with open("sample.txt","a") as f:
    f.write("Next new line.\n")

with open("sample.txt","r") as f:
    content = f.read()
    print(content)

#count total no of lines
with open("sample.txt","r") as f:
    lines = f.readlines()
    print(f"Total number of lines: {len(lines)}")