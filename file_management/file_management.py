import os

def load_template(file_name):
    with open(file_name,'r', encoding = 'utf-8') as f:
        return f.read()
    
#这个是加载内容：
content = load_template('file_management/name.txt')
content_2 = load_template('file_management/base.txt')
# print(content)
# print(content_2)

#此处进行替换
content_3 = content_2.replace('{ weight}', content)

print(content_3)

#把替换的结果存到third.txt里
with open('file_management/third.txt', 'w', encoding = 'utf-8') as f:
    f.write(content_3)