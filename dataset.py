import json, networkx as nx, pandas as pd, re, requests
from bs4 import BeautifulSoup

status = {
    'Best Current Practice': '#1f77b4',    # Blue
    'Draft Standard': '#ff7f0e',           # Orange
    'Experimental': '#9467bd',             # Purple
    'Historic': '#7f7f7f',                 # Gray
    'Informational': '#2ca02c',            # Green
    'Internet Standard': '#d62728',        # Red
    'Not Issued': '#bdbdbd',               # Light Gray
    'Proposed Standard': '#ffbb78',        # Yellow
    'Unknown': '#000000'                   # Black
}

htmlText = requests.get('https://www.rfc-editor.org/search/rfc_search_detail.php?page=All&pub_date_type=any&sortkey=Number&sorting=ASC').content
soup = BeautifulSoup(htmlText, 'lxml')

page = soup.find("table", class_="gridtable")
i = 0
items = []
for tr in page.find_all("tr"):
    if i == 0:
        i += 1
        continue
    j = 0
    content = []
    for td in tr.find_all("td"):
        if j == 0 or j == 2 or j == 4:
            content.append(td.text.strip())
        elif j == 5:
            if td.text.strip() == '':
                content.append('')
            else:
                content.append(td.text.replace('Errata, ','').replace('Errata','').strip())
        elif j == 6:
            content.append(td.text.split('(')[0].strip())
        j += 1
    items.append(content)
    i += 1
df = pd.DataFrame(items, columns=['RFC','Title','Date','Info','Status'])
for i, r in df.iterrows():
    if r['Status'] == None:
        df.iloc[i] = ['RFC\u00a01685','Writing X.400 O/R Names','August 1994','','Informational']
df["RFC"] = df["RFC"].str.extract(r'(?i)(RFC\s*\d+)', expand=False)

updatesPattern = r'(Updates|Updated\sby)\s(RFC\s\d+(?:,\sRFC\s\d+)*)'
obsoletesPattern = r'(Obsoletes|Obsoleted\sby)\s(RFC\s\d+(?:,\sRFC\s\d+)*)'

G = nx.Graph()
for i, r in df.iterrows():
    G.add_node(r["RFC"], title=f'{r["Title"]}', date=f'{r["Date"]}', status=f'{r["Status"]}', color=status[r['Status']], size=20)
for _, row in df.iterrows():
    if row['Info'] != '':
        updates = re.findall(updatesPattern, row['Info'])
        obsoletes = re.findall(obsoletesPattern, row['Info'])
        for i in updates:
            for j in i[1].split(', '):
                G.add_edge(row['RFC'], j)
        for i in obsoletes:
            for j in i[1].split(', '):
                G.add_edge(row['RFC'], j)
graph_data = {
    'nodes': [{'id': node, **data} for node, data in G.nodes(data=True)],
    'edges': [{'source': source, 'target': target} for source, target in G.edges()]
}

with open('graph_data.json', 'w') as f:
    json.dump(graph_data, f, indent=4)