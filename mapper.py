#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys

dictBest = ["Best", "best", "Very Good", "very good", "Amazing", "amazing"]
dictGood = ["Good", "good", "Do", "do"]
dictAverage = ["Average", "average", "Ok", "ok"]
dictBad = ["Bad", "bad", "issues", "Don't", "don't"]
dictWorst = ["Worst", "worst", "Very Bad", "very bad", "Useless","useless" ]

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
	
    for word in words:
        if(word in dictBest):
            print '%s\t%s' % ("Best", "1")
        elif(word in dictGood):
            print '%s\t%s' % ("Good", "1")
        elif(word in dictAverage):
            print '%s\t%s' % ("Average", "1")
        elif(word in dictBad):
            print '%s\t%s' % ("Bad", "1")
        elif(word in dictWorst):
            print '%s\t%s' % ("Worst", "1")
    
