valid_skyphrases = 0

with open('skychallenge_skyphrase_input.txt') as skyphrases:

	for line in skyphrases:

		words_in_line = line.split()
		length_of_line = len(words_in_line)
		line_without_duplicates = set(words_in_line)
		length_of_line_without_duplicates=len(line_without_duplicates)

		if length_of_line == length_of_line_without_duplicates:
			valid_skyphrases += 1

print(f'There are {valid_skyphrases} valid skyphrases!')