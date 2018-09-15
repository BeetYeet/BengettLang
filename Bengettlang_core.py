bl_high = (4*4*4)

'''
bl looks like this:
130110


charset:
0 : space
1-26 : a-z
27-37 : 0-9
38 : .
39 : !
40 : ?
41 : <Bengette>

'''
def text_to_bl(txt):
	bl = ''
	for x in range(0,len(txt)):
	
		i = char_to_int(txt[x])

		bl += get_bengett(int_to_bl(i))
	return bl

def char_to_int(c):
	inp = ord(c)
	if(inp <= ord('z') and inp >= ord('a')):
		return inp - ord('a') + 1
	if(inp == ord(' ')):
		return 0
	if(inp <= ord('9') and inp >= ord('0')):
		return inp - ord('0') + 27
	raise ValueError('Character Not In Charset')

def bengett(index):
	if(index == 0):
		return ':smolbegent:'
	if(index == 1):
		return ':bengett:'
	if(index == 2):
		return ':creeebegent:'
	if(index == 3):
		return ':megabegett:'
	raise ValueError('Bengett Index Out Of Range')

def int_to_bl(i):
	bl_out = ''
	i1 = 0 #1=1
	i2 = 0 #1=4
	i3 = 0 #1=16

	mod = 16
	work = i
	for m3 in range(1,4):
		num = work%mod
		if(num == work):
			#no fit
			break
		else:
			work -= mod
			i3 += 1


	mod = 4
	for m2 in range(1,4):
		num = work%mod
		if(num == work):
			#no fit
			break
		else:
			work -= mod
			i2 += 1


	mod = 1
	for m1 in range(1,4):
		num = work%mod
		if(num == work):
			#no fit
			break
		else:
			work -= mod
			i1 += 1

	return (str(i1) + str(i2) + str(i3))



def get_bengett(bl):
	s = ''
	i = 0
	while (i < len(bl)):
		s += ( bengett(int(bl[i+2])) + ' ' + bengett(int(bl[i+1])) + ' ' + bengett(int(bl[i])) + '\n')
		i += 3
	return s

