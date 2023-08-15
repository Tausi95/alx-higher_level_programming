#!/usr/bin/python3

#!/usr/bin/python3
def multiple_returns(sentence):
    # Calculate the length of the sentence
    # Use a conditional expression to determine the first character
    # if the sentence is not empty
    val = (len(sentence), sentence[0] if len(sentence) > 0 else None)
    return val
