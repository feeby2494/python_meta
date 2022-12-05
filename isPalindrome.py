
def isPalindrome(string):
	startIndex = 0
	endIndex = len(string) - 1

	for character in string:
		if startIndex == endIndex:
			return True
		if string[startIndex] != string[endIndex]:
			return False
		startIndex += 1
		endIndex -= 1		
	return True

if __name__ == "__main__":
	end = False
	while end is False:
		string = input("Give me a string to check if it's spelled the same backwards:\nType 'Q' to quit\n")
		if string.lower() == 'q':
			end = True
			break; 
		palindrome = isPalindrome(string)
		print("True, it's a palindrome" if palindrome is True else "False, it's not a palindrome")
