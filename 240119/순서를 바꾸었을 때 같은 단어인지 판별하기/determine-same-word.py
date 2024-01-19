word1 = input()
word2 = input()
word1 = ''.join(sorted(word1))
word2 = ''.join(sorted(word2))
if word1 == word2:
    print("Yes")
else:
    print("No")