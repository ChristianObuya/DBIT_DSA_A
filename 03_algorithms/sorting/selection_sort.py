def selection_sort(unsorted_list):
    number_of_items = len(unsorted_list)
    
    for outerloop in range(number_of_items):
        minimum_index = outerloop
        
        for innerloop in range(outerloop + 1, number_of_items):
            if unsorted_list[innerloop] < unsorted_list[minimum_index]:
                minimum_index = innerloop
                
        temp = unsorted_list[outerloop]
        unsorted_list[outerloop] = unsorted_list[minimum_index]
        unsorted_list[minimum_index] = temp
        
    return unsorted_list

values = [15,12, 12,60,5,7]
print(f"Unsorted List {values}")

sorted_list = selection_sort(values)
print(f"Sorted List {sorted_list}")