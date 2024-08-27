# Python code to create and store the list in a JavaScript file

import json

# Your Python list
python_list = [1, 2, 3, 4, 5]
value = [
    "Apple",
    "Bannan",
    "Papaya",
    "Grapes",
    "Orange",
    "WaterMelon",
    "Peach",
    "Mango"
]
value=[]
for i in range(10000):
    val=f"Item_{i}"
    value.append(val)

# Convert the Python list to JSON format
json_data = json.dumps(value)
print(json_data)
# Write JSON data to list.js file
with open('list.js', 'w') as f:
    f.write('const myList = ')
    f.write(json_data)
    f.write(';')

print("List stored in list.js file successfully!")
