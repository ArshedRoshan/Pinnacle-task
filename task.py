data = [{'d1': [1, 2, 3], 'd2': 2, 'd3': {'d4': [1, 23,2]}}, 1, 3,2]
count = 0

for item in data:
    if isinstance(item, int) and item == 2:
        count += 1
    elif isinstance(item, dict):
        for sub_item,values in item.items():
            
            if isinstance(values, int) and values == 2:  
                count += 1
            elif isinstance(values,list) and 2 in values:
                count += values.count(2)
            elif isinstance(values,dict):
                for value1,value2 in values.items():
                    if isinstance(value2,list) and 2 in value2:
                        count += value2.count(2)

print("Count of 2:", count)