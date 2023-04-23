import requests
from bs4 import BeautifulSoup

# 设置请求头，模拟浏览器访问
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 将结果保存到文件中
file = open('douban_top250.txt', 'w', encoding='utf-8')

# 访问前250页数据
for i in range(0, 250, 25):
    url = 'https://book.douban.com/top250?start={}'.format(i)
    # 发送请求并解析HTML
    r = requests.get(url, headers=header)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    # 获取书籍列表
    book_list = soup.find_all('tr', {'class': 'item'})
    # 遍历书籍列表，获取书名、作者、出版社和出版日期等信息
    for book in book_list:
        title = book.find('div', {'class': 'pl2'}).find('a')['title']
        href = book.find('div', {'class': 'pl2'}).find('a')['href']
        author_info = book.find('p', {'class': 'pl'}).get_text().split('/')
        author = author_info[0].strip() # 作者
        press = author_info[-3].strip() # 出版社
        date = author_info[-2].strip()  # 出版日期
        rate = book.find('span', {'class': 'rating_nums'}).get_text() # 评分
        print(title + '|' + author + '|' + press + '|' + date + '|' + rate + '|' + href + '\n')
        # 将结果保存到文件中
        file.write(title + '|' + author + '|' + press + '|' + date + '|' + rate + '|' + href + '\n')

# 关闭文件
file.close()
print('爬取成功！')