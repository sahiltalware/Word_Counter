# Function to count words in a given text
def word_count(text):

    # Check if the text is not empty
    if not text:
        return 0

    # Split the input text into a list of words using the default space delimiter
    words = text.split()
    
    # Return the count of words in the list
    return len(words)


# Get input text from the user
input_text = input("Enter a sentence or paragraph :")

# Call the word_counter and store the result in word_count
result = word_count(input_text)

# display the word count to the user
print("Number of words are:", result)

