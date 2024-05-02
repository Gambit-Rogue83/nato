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


def generate_phonetic():
    street_name = input("Enter your name: ").upper()

    try:
        nato_name = [nato_alpha[letter] for letter in street_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(nato_name)


generate_phonetic()