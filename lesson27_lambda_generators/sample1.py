# def calc(a,b, action):
#     result = action(a,b)
#     print(f"result = {result}")
    
# calc(3, 5, lambda x,y: x-y)

FILTER_EVEN=1
FILTER_ODD=2

def list_filter(my_list, func_filter):
    filtered_list = []
    
    for item in my_list:
        if func_filter(item)==True:
            filtered_list.append(item)
    
    return filtered_list


def list_filter(my_list, type_filter):
    filtered_list = []
    
    for item in my_list:
        if type_filter ==FILTER_EVEN:
            if item%2==0:
                filtered_list.append(item)
        elif type_filter ==FILTER_ODD:
            if item%2!=0:
                filtered_list.append(item)
    
    return filtered_list


my_list = [23,4,45,3,23,23,43,54,76,34,12,267,9,3,3]
print(my_list)

filtered_list_even = list_filter(my_list, lambda item: item%2==0)
print(filtered_list_even)

filtered_list_odd = list_filter(my_list, lambda item: item%2!=0)
print(filtered_list_odd)

filtered_list_gt_100= list_filter(my_list, lambda item: item>100)
print(filtered_list_gt_100)