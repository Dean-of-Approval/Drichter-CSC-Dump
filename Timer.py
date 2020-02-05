import time
start = time.time()
def anagramSolution3(s1,s2):
	return anagramRec("",s1,s2)

def anagramRec(so_far, remaining, target):
	if len(remaining) == 0:
		return so_far == target
	for i in range(len(remaining)):
		whats_left = remaining[0:1] + remaining[i+1:]
		if anagramRec(so_far + remaining[i], whats_left, target):
			return True
	return False

anagramSolution3("abcd","dcab")
stop = time.time()

totaltime = stop-start

print(totaltime)

