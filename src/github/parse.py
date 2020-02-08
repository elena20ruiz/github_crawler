from src.github import GITHUB_URL
from bs4 import BeautifulSoup

def search_result(content):
    soup = BeautifulSoup(content, 'html.parser')
    
    repo_list = soup.find("ul", class_="repo-list")
    repo_elements = repo_list.find_all("li")
    
    output = []
    for el in repo_elements:
        link = el.find('a')
        element = {
            'url': GITHUB_URL + link['href']
        }
        output.append(element)
    return output



def additional_info_result(content):
    soup = BeautifulSoup(content, 'html.parser')

    result = {
        'language_stats': {},
        'owner': ''
    }

    main = soup.find('main')
    result['owner'] = main.find('h1').find('a').getText()

    summary = main.find('summary')
    languages = summary.find_all('span')

    for l in languages:
        if 'aria-label' in l.attrs:
            aria = l['aria-label']
            info = aria.split(' ') 

            name_lang = info[0]
            pert_lang = float(info[1].replace('%', ''))
            result['language_stats'][name_lang] = pert_lang
    return result