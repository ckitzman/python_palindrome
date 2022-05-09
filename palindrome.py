''' Want to see if your string is a Palindrome (reads the same backwards as forwards)? You may never need this, but it sure is interesting! ''' 
message = #Enter a word to see if it is a palindrome
inverse = message[::-1] 
if message == inverse:
    print(message,'is a palindrome') 
else: print(message,'is not a palindrome')