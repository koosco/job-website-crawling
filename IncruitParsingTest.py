from bs4 import BeautifulSoup

with open('resources/test.html', encoding='utf-8') as file:
    html_content = file.read()

tags = []
soup = BeautifulSoup(html_content, 'html.parser')
content_list = soup.find('div', {'class': 'cBbslist_contenst'})
contents = content_list.find_all('ul', {'class': 'c_row'})

for content in contents:
    cell_first = content.find('div', {'class': 'cell_first'})
    cell_mid = content.find('div', {'class': 'cell_mid'})
    cell_last = content.find('div', {'class': 'cell_last'})

    company_name = cell_first.find('a', {'class': 'cpname'})  # 회사명
    announcement_name = cell_mid.find('div', {'class': 'cl_top'}).find('a')  # 공고명

    spec = cell_mid.find('div', {'class': 'cl_md'}).find_all('span')
    career = spec[0]  # 경력
    education = spec[1]  # 교육수준
    location = spec[2]  # 지역
    work_type = spec[3]  # 직무형태

    company_tags = cell_mid.find('div', {'class': 'cl_btm'}).find_all('span')
    for tag in company_tags:
        tags.append(tag)
    tags = list(map(lambda x: x.text, tags))

    deadline = cell_last.find('span')

    print(company_name.text)
    print(announcement_name.text)
    print(career.text)
    print(education.text)
    print(location.text)
    print(work_type.text)
    print(tags)
    print(deadline.text)
    break
