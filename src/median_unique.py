import os
import time
# os.chdir("..")
f = open("tweet_input/tweets.txt", "r").read().split()

unique_words = {}
for word in f:

	if word in unique_words:
		
		unique_words[word] += 1
	else:
		unique_words[word] = 1


# for k,v in unique_words.iteritems():
# 	print(k,v)

ft1 = open("tweet_output/ft1.txt", "w")
for k,v in sorted(unique_words.iteritems()):
	ft1.write(str((k,v))+'\n')

ft1.close()