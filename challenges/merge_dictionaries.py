# Merge the following to dictionaries into one:
name1 = {"Kelly": 23, "Derick": 14, "John": 7, "Panjeet": 37}
name2 = {"Ravi": 45, "Eric": 67}

names1 = name1 | name2
print(
    names1
)  # {'Kelly': 23, 'Derick': 14, 'John': 7, 'Panjeet': 37, 'Ravi': 45, 'Eric': 67}

names2 = {**name1, **name2}
print(
    names2
)  # {'Kelly': 23, 'Derick': 14, 'John': 7, 'Panjeet': 37, 'Ravi': 45, 'Eric': 67}
