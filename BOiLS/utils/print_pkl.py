import pickle

play_file = ''
ref_file  = ''

with open(play_file, 'rb') as f:
    data = pickle.load(f)

print('== total number: ', len(data))

for key, value in data.items():
    print(key, value[0], value[1], value[0]+value[1])

with open(ref_file, 'rb') as f:
    data = pickle.load(f)
print(data)