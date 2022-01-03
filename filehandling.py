# with open('data.txt', 'r') as f:
#     # print(f.read()) 
#     #readline() reads 1 line only
#     print(f.read(10))

# Another way of doing this is by open and close function. 
#Here, function should be necessarily closed. So this way is not preferred 
#as there can be errors before close() and then close will not work.

# f = open('data.txt', 'r')
# f.read()
# f.close

#Similarly, We have for write and append as well
# f.write()  ,  f.writeline()