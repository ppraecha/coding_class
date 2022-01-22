file_read = open("./data.txt", "r")

get_input = file_read.readline()
print(get_input.split())
get_input = file_read.readline()
print(get_input.split())
file_read.close()

file_write = open("./data.txt", "w")

string = "100 200"
file_write.write(string)

file_write.close()
