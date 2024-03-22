#my_file = open("text.txt", "r")

#print(my_file.read(4))
#print(my_file.readline())
#print(my_file.readline())

#line_by_line1 = my_file.read().splitlines()
#print(line_by_line1)
#my_file.close()

# with open('text.txt', 'r') as f:
#     #print(f.readline())
#     for line in f:
#         print(line)

#f = open("towritein.txt", "x")
with open('towritein.txt', 'w') as f:
    for i in range(10):
        f.write("68\n")
    f.write("833")