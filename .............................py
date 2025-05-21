
# Tuple multiplication

# initialize tuples
tup1 = (4,3,2,2,-1,18)
tup2 = (2,4,8,8,3,2,)

# printing original tuples
print("The original tuple 1 : " + str(tup1))
print("The original tuple 2 : " + str(tup2))

# Tuple multiplication
res = []
for i in range(0, len(tup1)):
    res.append(tup1[i] * tup2[i])
res = tuple(res)

# printing result
print("The multiplied tuple : " + str(res))

