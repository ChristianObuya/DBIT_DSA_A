def bubble_sort(unsorted_list):
    number_of_items = len(unsorted_list)
    
    for outerloop in range(number_of_items):
        for innerloop in range(0, number_of_items - 1 - outerloop):
            if unsorted_list[innerloop] > unsorted_list[innerloop + 1]:
                # swap the values if the current value is larger than the next value
                temp = unsorted_list[innerloop]
                unsorted_list[innerloop] = unsorted_list[innerloop + 1]
                unsorted_list[innerloop + 1 ] = temp
            
            # print(f"Inner loop {unsorted_list}")  
        # print(f"Outer loop {unsorted_list}")
  
    return unsorted_list

values = [5,4,3,2,1]
print(f"Unsorted List {values}")

sorted_list = bubble_sort(values)
print(f"Sorted List {sorted_list}")