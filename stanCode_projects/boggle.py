"""
File: boggle.py
Name: Sean Wang
----------------------------------------
This program recursively finds all answer in boggle game
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	make a boggle game
	"""

	row_lst = row_input()
	# row_lst: [['a', 'b', 'c', 'd'],.....]
	if len(row_lst) == 4:
		start = time.time()
		####################
		dict_lst = read_dictionary()
		n = 0
		for i in range(len(row_lst)):
			for j in range(len(row_lst[i])):
				n += boggle(row_lst, '', [], dict_lst, [], i, j, i, j, row_lst[i][j])
		print(f'There are {n} words in total.')
		####################
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def row_input():
	row_lst = []
	for i in range(4):
		row = input(f"{i+1} row of letters: ").lower()
		if len(row) != 7 or row[1] != ' ' or row[3] != ' ' or row[5] != ' ' \
			or not row[0].isalpha() or not row[2].isalpha() or not row[4].isalpha() or not row[6].isalpha():
			print('Illegal input')
			break
		row_lst.append(row.split())
	return row_lst


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dict_lst = {}
	with open(FILE, 'r') as f:
		for line in f:
			if len(line[:-1]) >= 4:
				dict_lst[line[:-1]] = True
	return dict_lst


def boggle(row_lst, ans, ans_lst, dict_lst, repeat_lst, record_i, record_j, i, j, begin_word):
	if ans in dict_lst and dict_lst[ans]:
		dict_lst[ans] = False
		ans_lst.append(ans)
		print(f'Found: \"{ans}\"')
	if row_lst[i][j] != ' ':
		# Choose
		ans += begin_word
		row_lst[i][j] = ' '
	for k in range(-1, 2):
		for m in range(-1, 2):
			if 0 <= record_i+k <= 3 and 0 <= record_j+m <= 3:
				# Choose letter surround [record_i][record_j]
				if row_lst[record_i+k][record_j+m] != ' ' and (record_i+k != record_i or record_j+m != record_j):
					# Choose
					ans += row_lst[record_i+k][record_j+m]
					if ans not in repeat_lst:
						if has_prefix(ans, dict_lst):
							# Choose
							record_i = record_i + k
							record_j = record_j + m
							row_lst[record_i][record_j] = ' '
							# Explore
							boggle(row_lst, ans, ans_lst, dict_lst, repeat_lst, record_i, record_j, i, j, begin_word)
							# Un-choose
							row_lst[record_i][record_j] = ans[-1]
							record_i = record_i - k
							record_j = record_j - m
						else:
							repeat_lst.append(ans)
					# Un-choose
					ans = ans[:-1]
	if record_i == i and record_j == j:
		# Un-choose
		row_lst[i][j] = begin_word
	return len(ans_lst)


def has_prefix(sub_s, dict_lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dict_lst: (lst)
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_lst:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
