# LISTS
def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
print(find_largest([4,2,5,8,1]))  # Output: 8

def second_largest(numbers):
    unique_sorted=sorted(set(numbers), reverse=True) # sorts the numbers in desc order
    if len(unique_sorted) < 2:
        return None  # Return None if there is no second largest number
    return unique_sorted[1]
print(second_largest([4,7,3,10,1])) # Output: 7

def remove_duplicates(numbers):
    return list(set(numbers))  
print(remove_duplicates([4,2,5,8,1,2,4]))  # Output: [1,2,4,5,8]

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst
print(reverse_list([1,2,3,4,5]))  # Output: [5,4,3,2,1]

def common_elements(list1,list2):
    return list(set(list1) & set(list2)) 
print(common_elements([1,6,3,5], [3,7,9,6]))  # Output: [3, 6]

# TUPLES
numbers_tuple = (1,6,3,5,4,5,9)
print(numbers_tuple.count(5))  # Output: 2

t = (1,8,2,6)
lst = list(t)        # tuple to list
print(lst)            # [1,8,2,6]

back_to_tuple = tuple(lst)   # list to tuple
print(back_to_tuple)          # (1,8,2,6)

#SETS
nums = [11,5,15,13,8,8,5]
unique_values = set(nums)
print(unique_values)   # {11,5,15,13,8}

set1 = {11,32,13,24}
set2 = {32,45,61,11}

print(set1 | set2)   # union: {11,32,13,24,45,61}
print(set1 & set2)   # intersection: {32,11}

#DICTIONARIES
student = {
    "name": "Mahnoor", 
    "age": 20,
    "grades": [85,90,78]
}
print(student)  # Output: {'name': 'Mahnoor', 'age': 20, 'grades': [85,90,78]}

students = {
    "Ali": [85,90,78],
    "Sara": [95,85,88],
    "Zainab": [70,75,80]
}

def average(marks_list):
    return sum(marks_list) / len(marks_list)

for name, marks in students.items():
    print(f"{name}'s average: {average(marks):.2f}")

# Output:
# Ali's average: 84.33
# Sara's average: 89.33
# Zainab's average: 75.00

def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        word = word.strip(".,!?")   # remove punctuation
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

sentence = "the dog is barking at the boy. the boy is scared!!"
print(word_frequency(sentence))
# {'the': 3, 'dog': 2, 'is': 2, 'barking': 1, 'at': 1, 'boy': 2, 'scared': 1}


