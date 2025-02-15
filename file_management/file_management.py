import os

def load_template(file_name):
    with open(file_name,'r', encoding = 'utf-8') as f:
        return f.read()
    
    
#这个是加载内容：
base = load_template('file_management/base.html')
project_website = load_template('file_management/project_website.html')

#此处进行替换
index = base.replace('{personal-website}', project_website)

#把替换的结果存到third.txt里
with open('file_management/index.html', 'w', encoding = 'utf-8') as f:
    f.write(index)