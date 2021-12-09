def find(input_list,input_str):
    ans = []
    
    if len(input_list) == 0:
        return ans

    for dc in input_list:

        for k,v in dc.items():
            if input_str in str(v):
                ans.append(dc)
                break
    
    return ans
            
input_list = [{
   "name": "Jatin",
   "email": "jatinparekh93@gmail.com",
   "age": 20
}, {
   "name": "Yolo",
   "email": "Forever@gmail.com",
   "dob": 2020
}, {
   "name": "ParekhJatin",
   "email": "jatinparekh93@yahoo.com",
   "age": 20
}]

            
print(find(input_list, "20"))  # print a list of 1st and 3rd dict
print(find(input_list, "yahoo")) # print a list with only 3rd dict



