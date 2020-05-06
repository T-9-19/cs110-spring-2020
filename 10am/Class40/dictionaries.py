"""
    Darren Strash
    dictionaries.py
    May 06, 2020
    Experiments with dictionaries and file reading
"""

# Storing and querying associative data.

# key, value pairs

#mapping (association) between names and ages
# "Darren" -> 36, "Beyonce" -> 38

# name_age_tuples = [("Darren", 36), ("Beyonce", 38)]
#
# #Get age associated with name "Beyonce"?
# for (name, age) in name_age_tuples:
#     if name == "Beyonce":
#         print("{} is {} years old".format(name, age))
#         break

# A dictionary: It's a data structure to store (unordered) associative data
# which is a mapping from a key to a value.

#name_to_age = {"Darren" : 36, "Beyonce" : 38}

#For a key, can only store one value!
#name_to_age = {"Darren" : 36, "Beyonce" : 38, "Beyonce" : 40}
#overwrites Beyonce's age to 40.

# print("{} is {} years old".format("Beyonce", name_to_age["Beyonce"]))

# print(name_to_age)

# How does this work without ordering keys?

# Can treat each letter as a number
# D = 4
# a = 1
# r = 19
# r = 19
# e = 5
# n = 14

# Then combine to form an index into a list, called a hash_value.
# hash, since chopping up the key
# e.g., sum the values 62 -> index into a list. Need to handle colliding indices

# Can print out the list of keys
# print(name_to_age.keys())

#Application: Analyzing word or character frequency
#How to dictionaries to count words? -> are there any challenges?

# word_frequency = {}
# sentence = "Is that all there is it is all that there is"
# for word in sentence.split():
#     #print(word)
#     if word in word_frequency:
#         word_frequency[word.lower()] += 1
#     else:
#         word_frequency[word.lower()] = 1
#
# print(word_frequency)

#Analyzing the word frequency of Les Miserables
word_frequency = {}
file = open("lesmis.txt", "r")

for line in file:
    line = line.strip()
    for word in line.split():
        while word != "" and not word[-1].isalpha():
            word = word[0:len(word)-1]
        while word != "" and not word[0].isalpha():
            word = word[1:]

        if word == "":
            continue

        #print(word)
        if word.lower() in word_frequency:
            word_frequency[word.lower()] += 1
        else:
            word_frequency[word.lower()] = 1

print(word_frequency)

most_frequent_word = None
most_frequent_count = 0

for word in word_frequency.keys():
    if most_frequent_count < word_frequency[word]:
        most_frequent_word = word
        most_frequent_count = word_frequency[word]

print("{} appeared {} times. ".format(most_frequent_word, most_frequent_count))
