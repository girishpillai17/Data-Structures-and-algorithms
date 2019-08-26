
"""Create a function called word_split() which takes in a string phrase and a set 
list_of_words. The function will then determine if it is possible to split the string 
in a way in which words can be made from the list of words. You can assume the phrase 
will only contain words found in the dictionary if it is completely splittable."""


def word_split(phrase, list_of_words, output = None):
    if output is None:                         #Check to see if the output has been initiated
        output = []

    for word in list_of_words:                 #Check every word from the list_of_words
         
         if phrase.startswith(word):           #To check if the phrase starts with the word
             output.append(word)               #If yes the append the word to the output list

             return word_split(phrase[len(word):], list_of_words, output)
                                               #recursively works on the remaining phrase
    return output

print(word_split('themenranaway',['the','ran','man']))

         
