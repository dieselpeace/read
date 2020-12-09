import random
import time
import progressbar

data = [] 
count = 0 
bar = progressbar.ProgressBar(max_value=1000000)							#declare list
with open('reviews.txt', 'r') as s: #open reviews.txt
	for line in s: 					#every entry in .txt
		data.append(line)			#put it in the list
		count += 1
		bar.update(count) 			
print(len(data)) 					#length of the list

sum_data = 0 						#declare sum_data
for d in data: 						#take every entry in data
	sum_data += len(d) 				#add it together
print(sum_data/len(data)) 

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('there are', len(new), 'reviews with less than 100 words')
print(new[random.randint(1,1000)])

good = [a for a in data if 'good' in a]
print(good[random.randint(1,1000)])


#word count
start_time = time.time()
wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000:
		print(word,wc[word])
end_time = time.time()
print(end_time - start_time, 'secs')

while True:
	word = input('what word do you want to search: ')
	if word == 'q':
		break
	if word in wc:
		print(wc[word])
	else:
		print('word is not there')

