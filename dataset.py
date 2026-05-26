import json, networkx as nx, pandas as pd, re, requests
from datetime import datetime
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

i = 1
items = []
while(True):
    jsoncontent = requests.post(url = 'https://typesense.ietf.org/multi_search?x-typesense-api-key=0C8Exv9grP2li1fwQeg34nPtKfccC3Qa',
                                data = f'''{{
  "searches": [{{
    "preset": "red",
    "sort_by": "publicationDate:desc",
    "collection": "docs",
    "q": "*",
    "facet_by": "area.full,authors.name,flags.hiddenDefault,group.full,publicationDate,status.name,stream.name",
    "max_facet_values": 1,
    "page": {i},
    "per_page": 250
  }}]
}}''').json()
    total = jsoncontent['results'][0]['found']
    
    pages = jsoncontent['results'][0]['hits']
    for page in pages:
        info = ''
        if page['document']["obsoletedBy"]:
            info += "Obsoleted by " + ", ".join(f'RFC {item}' for item in page["document"]["obsoletedBy"])
        if page['document']["updatedBy"]:
            info += 'Updated by ' + ", ".join(f'RFC {item}' for item in page["document"]["updatedBy"])
        items.append([
            page['document']['rfcNumber'],
            page['document']['title'],
            datetime.fromtimestamp(page['document']['publicationDate']),
            info,
            page['document']['status']['name']
        ])
    if(i * 250 >= total):
        break
    print(f'{i*250}/{total}')
    i += 1
df = pd.DataFrame(items, columns=['RFC','Title','Date','Info','Status'])

print(f'Total RFCs: {total}')
print(f'Total pages: {i}')

updatesPattern = r'(Updates|Updated\sby)\s(RFC\s\d+(?:,\sRFC\s\d+)*)'
obsoletesPattern = r'(Obsoletes|Obsoleted\sby)\s(RFC\s\d+(?:,\sRFC\s\d+)*)'

G = nx.Graph()
for i, r in df.iterrows():
    G.add_node(f'RFC {r["RFC"]}', title=f'{r["Title"]}', date=f'{r["Date"]}', status=f'{r["Status"]}', color=status[r['Status']], size=20)
for _, row in df.iterrows():
    if row['Info'] != '':
        updates = re.findall(updatesPattern, row['Info'])
        obsoletes = re.findall(obsoletesPattern, row['Info'])
        for i in updates:
            for j in i[1].split(', '):
                G.add_edge(f'RFC {row["RFC"]}', j)
        for i in obsoletes:
            for j in i[1].split(', '):
                G.add_edge(f'RFC {row["RFC"]}', j)
graph_data = {
    'nodes': [{'id': node, **data} for node, data in G.nodes(data=True)],
    'edges': [{'source': source, 'target': target} for source, target in G.edges()]
}

with open('graph_data.json', 'w') as f:
    json.dump(graph_data, f, indent=4)