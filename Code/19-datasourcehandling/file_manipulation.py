# file = open('./Course1401/Code/19-datasourcehandlig/our_file.txt','w')
file = open('our_file.txt','r')

content_lines = file.readlines()

for content in content_lines:
    if str(content).strip() == '1':
        continue

    print(':) ',content)

file.close()

with open('test.txt','w') as f:
    f.write('helloooo!')
    
# print(content)