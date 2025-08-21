# Daniel Soriano

fname = input("Enter file: ")
if len(fname) < 1: fname = 'clown.txt' # if no file name is provided
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        # looks for the word/key in the dictionary if not found value is 0
        # else add one to the value if key is found
        di[w] = di.get(w,0) + 1

# print(di)

# now we want to find the most common word
largest = -1 # assigned -1 in case of zero being a number in the dictionary
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k #capture/remember the key that was largest

print(theword, largest)