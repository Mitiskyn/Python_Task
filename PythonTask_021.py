list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
set = set()

for i in list: 
    for j in i.keys(): 
        set.add(i[j])

print(set)