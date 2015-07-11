import os
import time
# os.chdir("..")
lines = [line.rstrip('\n') for line in open('tweet_input/tweets.txt')]
words_tweeted = []
ft2 = open("tweet_output/ft2.txt", "w")

for i in lines:
	words_tweeted.append(len(i.split()))
	length = len(words_tweeted)
	
	#if even, then median is sum of middle two elements / 2
	if length % 2 == 0:
		median = (words_tweeted[(length-1)/2]+words_tweeted[((length-1)/2)+1])/float(2)
		#write to file
		ft2.write("{0:.2f}".format(median)+'\n')
	
	#if odd, then median is middle element: (n-1/2)
	#(1,2,3,4,5) (5-1/2) = 2 
	else:
		median = words_tweeted[(length-1)/2]
		#write to file
		ft2.write("{0:.2f}".format(median)+'\n')
		


	
ft2.close()

