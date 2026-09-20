test_dict = {"codingal": 2, "is": 3, "best": 2, "for": 4, "coding": 1}

print("the original dictionary ;" + str(test_dict))

k = 5

res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res+1

print("Frequesncy of k is : " +str(res))

