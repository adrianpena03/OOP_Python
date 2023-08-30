def ReadAndFix():
    clean_content = []
    with open ("/Users/adrianpena/Desktop/cat.txt", "r") as f:
        for line in f:
            x  = line.strip().split(";")
        clean_content.append(x)
        return clean_content
print(ReadAndFix())


# Step 1: Read File
# Step 2: Remove new line characters from each of the 3 items in a line
# Step 3: Remove awkward (variable) Spaces between all words


