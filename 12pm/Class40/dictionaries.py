"""
    Darren Strash
    dictionaries.py
    May 06, 2020
    Experiments with dictionaries and file reading
"""

# storing associative data -> key, value pairs
# "Darren" -> 36, "Beyonce" -> 38

# The slow and messy way: store tuples in lists
# name_age_list = [("Darren", 36), ("Beyonce", 38)]
#
# for (name, age) in name_age_list:
#     if name == "Beyonce":
#         print("{} is {} years old".format(name, age))
#         break


# The fast and clean way, map keys to values using a dictionary
#keys -> any immutable type
#values -> any Python object
# name_to_age = { "Darren"  : [36, "Is a professor"],
#                 "Beyonce" : 38 }

# print("{} is {} years old".format("Beyonce", name_to_age["Beyonce"]))

# Underneath the hood, dictionaries are unordered!!!!
# They use the value of the key to produce an index, simple example of
# strategy:

#D = 4
#a = 1
#r = 19
#r = 19
#e = 5
#n = 14

#sum = 62 -> index into a list where we store 36
# hash value

#Can use "in" to determind if a given key is in the dictionary
#print("Darren" in name_to_age)

# A popular application of dictionaries is counting frequency of words in
# a text.

# word_frequency = {}
# sentence = "Is that all there is yes it is maybe it is"
#
# for word in sentence.split():
#     if word.lower() in word_frequency:
#         word_frequency[word.lower()] += 1
#     else:
#         word_frequency[word.lower()] = 1
#
# print(word_frequency)

#Now let's analyze a bigger text that has punctuation: Les Miserables
word_frequency = {}

file = open("lesmis.txt")
for line in file:
    #print(line.strip())
    for word in line.split():
        while word != "" and not word[-1].isalpha():
            word = word[0: len(word) - 1]

        while word != "" and not word[0].isalpha():
            word = word[1:]

        if word == "":
            continue

        if word.lower() in word_frequency:
            word_frequency[word.lower()] += 1
        else:
            word_frequency[word.lower()] = 1

print(word_frequency)

# Largest frequency word is "the"!
# largest_frequency = 0
# largest_frequency_word = None
#
# for word in word_frequency.keys():
#     if largest_frequency < word_frequency[word]:
#         largest_frequency = word_frequency[word]
#         largest_frequency_word = word
#
# print("The most frequent word is {}, which appears {} times."
#           .format(largest_frequency_word, largest_frequency))
#

#Words with "high" frequency include marius, vajean, but no javert!
frequency_threshold = 1000

for word in word_frequency.keys():
    if frequency_threshold <= word_frequency[word]:
        print("Word '{}' appears {} times."
                     .format(word, word_frequency[word]))
