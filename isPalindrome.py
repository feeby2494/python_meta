
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


print(isPalindrome('racecar'))
