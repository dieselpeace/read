import random
data = [] 							#declare list
with open('reviews.txt', 'r') as s: #open reviews.txt
	for line in s: 					#every entry in .txt
		data.append(line) 			#put it in the list
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
print(new[1])

good = [a for a in data if 'good' in a]
print(good[random.randint(1,1000)])
