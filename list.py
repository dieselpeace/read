data = []
with open('reviews.txt', 'r') as s:
	for line in s:
		data.append(line)
print(len(data))

sum_data = 0
for d in data:
	sum_data += len(d)
print('average length of reviews: ', sum_data/len(data))
