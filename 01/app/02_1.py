import numpy as np

np.random.seed(0)

# x1 = np.random.randint(10, size=6)
# x2 = np.random.randint(10, size=(3,4))

# print(x2)
# print("---------------")
# print(x2[:2,:2])

# x = [1, 2, 3, 99, 99, 3, 2, 1]
# x1, x2, x3 = np.split(x, [1,3])

# print(x1, x2, x3)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x_split = np.split(x, [4,5])
# print (x)



# # # print(x)
# # # print(x_split)
# print(x_split[1])
# x_split[1] = 99
# print(x)
# print(x_split)

x = np.array([1,2,3])
y = np.array([3,2,1])
z = [99,99,99]

print(np.concatenate([x,x]))

