# add up and print the sum of all minimums.
# sort contents of every array.
array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# iterated 1st dimension of array
sum = 0
for a in array: 
#sort through each 2D array
    a.sort() # O(logn)
    sum += a[0]

print(sum)

test_dict = {}
test_dict[1] = 111
test_dict[2] = 222
test_dict[3] = 333

test_set = set(test_dict)

print(test_set)