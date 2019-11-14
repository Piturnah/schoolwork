sequence = input("Enter a sequence of words")

def sort(sequence):
    # separate sequence into array of words
    sequence = sequence.split()

    # remove duplicate words
    remove_duplicates(sequence)

    # bubble sort into alphanumerical order
    sequence = bubble_sort(sequence)
    
    for word in sequence:
        print(word + " ", end="")

def swap_positions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

# takes array as argument and returns it sorted
def bubble_sort(array):

    for i in range (0, len(array)):

        # don't sort already sorted elements
        for j in range (0, len(array) - i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j+1], array[j]

    return array

# takes array as argument and returns it without repeated elements
def remove_duplicates(array):

    for element in array:
        if array.count(element) > 1:
            del array[array.index(element)]

    return array

sort(sequence)
