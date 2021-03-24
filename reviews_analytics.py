
data = []
count = 0
length = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
	i = 0
	while i < len(data):
		length = length + len(data[i])
		i += 1
print('The average lengrh of the reviews is', length / len(data)) 
print('File read completed. There are ', len(data), 'records in total. ')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are ', len(new), 'data with less than 100 words.')