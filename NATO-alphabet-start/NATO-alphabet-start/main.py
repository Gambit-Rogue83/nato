#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alpha = {row.letter: row.code for (index, row) in nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
street_name = input("Enter your name: ").upper()

for letter in street_name:
    nato_name = [nato_alpha[letter] for letter in street_name]

