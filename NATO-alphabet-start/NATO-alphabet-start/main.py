student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(key)
    # print(value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(index)
    # print(row)
    #Access row.student or row.score
    # print(row.student)
    # print(row.score)
    pass

for (index, row) in student_data_frame.iterrows():
    new_dict = {row.student:row.score for (index, row) in student_data_frame.iterrows()}
    pass

print(new_dict)



# Keyword Method with iterrows()
# new_dict = {student:score for (student, score) in student_data_frame.iterrows()}
# print(new_dict)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("What is your word?").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please, enter a letter from the alphabet")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()