# get the input word from command line
input_word = raw_input("Input a word: ")
# read the input file
valid_words = open("words.txt", "r")
# iterate the file, line by line
for valid_word in valid_words:
	# remove the extra line break from file reading
	# convert the word to lower case
	# convert the word to a list of characters
	word_array = list(valid_word.replace("\n", "").lower())
	# convert the input word to lower case
	# convert the input word to a list of characters
	input_word_array = list(input_word.lower())
	# skip current iteration if current word is longer than the input word
	if len(word_array) > len(input_word_array):
		continue
	# a boolean flag
	match = True
	# iterate the letters of the word from file one by one
	for letter in word_array:
		# check if currrent letter is in the input word array
		if letter in input_word_array:
			# if found, delete the letter
			input_word_array.pop(input_word_array.index(letter))
		else:
			# letter was not found, therefore, the current word is not in the input word
			match = False
			# stop the innermost loop, no need to iterate further
			break
	# print only if match = True
	if match:
		print valid_word.replace("\n", "")
# always close the file
valid_words.close()
