import glob
txt_files = glob.glob("*.txt")

data = {}

def read_data(file):
    with open(file, encoding='utf-8') as f:
        result = f.read()
    return result

for file in txt_files:
    with open(file, encoding='utf-8') as f:
        line_count = 0
        for line in f:
            line_count += 1
    data[file] = {'count': line_count, 'read': read_data(file)}
sorted_data = sorted(data.items(), key=lambda x: x[1]['count'])
dic = dict(sorted_data)


for key, value in dic.items():
    result = f'{key} \n{dic[key]["count"]} \n{dic[key]["read"]}'
    print(result)

