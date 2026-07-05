file = open("details.txt", "w")
file.write("lorem ipsum")
file.close()

# r  - Read
# w  - Write (overwrite existing content or create new file)
# a  - Append (add data at the end or create new file)

# r+ - Read + Write (file must already exist)
# w+ - Write + Read (overwrite existing content or create new file)
# a+ - Append + Read (create file if it doesn't exist)