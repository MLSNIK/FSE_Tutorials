age_list = [21, 23, 23]

def age_print(list):
    new_list = []
    for i in age_list:
        #print(i)
        
        if i in new_list:
            print(f"{i} age is in the list")
        else:
            print(f"{i} age is not in the list")
        new_list.append(i)
        
age_print(age_list)

#mistake because the 23 is in the list initially 