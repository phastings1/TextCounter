#############
'''
f = open(file_name)
total = 0
for line in f:
    if "apple" in line:
        total += 1
f.close()
print total
'''
#############
dtprnt = 'What word are we searching for?'
matra = 'The total number of '
isx =  '  is  '
warnuser = 'If you did not find what you are looking for,\n remember that this is case sensitive.'
oki = 'ok'
fnprint = 'CURRENTLY NONOPERATIONAL: What file would you like to open?'
#############



print (dtprnt)
datas = input()
print = (oki)
print =(fnprint)
fn = input()
print (oki)

#############
f = open("ex20150609.log", "r")
wcount = 0
for line in f:
    if datas in line:
        wcount += 1
f.close()
print (matra + datas+ isx, wcount)
print (warnuser)
