###### Amazon ######
# Given a list of numbers delete all numbers that create a sequence of 3 identical digits
# e.g. [1,1,2,2,3,3,3,2,1] -> [], [2,2,2,3,1,3,7,7,7] -> [3,1,3]
# What if you parameterize the length of the run to be deleted?



# Create the classes and interfaces for a library that replicates the functionality of the Linux find command


# Given a list of words and an NxN grid of letters, determine which of the words can be formed by traversing up, down, right, or left


### Ramp ###
# convert snake case to camelCase. Any leading or trailing underscores should be preserved, for example __variable_name__ would be changed to __variableName__, _variable_two would be _variableTwo, and variable_three would be variableThree
def snake_to_camel(text):
    words = text.split()
    def convert_word(word):
        # Variable names
        if '_' in word:
            parts = word.split('_')
            # Keep track of whether we are past the first word and need to begin capitalizing
            first_word = True
            for i, part in enumerate(parts):
                # Replace empty strings with underscores
                if part == '':
                    parts[i] = '_'
                # Capitalize everything after the first word
                elif not first_word:
                    parts[i] = part.capitalize()
                # On the first word, set the flag to false and make no changes to it
                else:
                    first_word = False
            return ''.join(parts)
        # Other words
        return word

    converted_words = [convert_word(word) for word in words]
    result = ' '.join(converted_words)

    return result