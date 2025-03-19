import pandas as pd
import lxml

path = 'wiki.html'

html_raw = pd.read_html(path)

top_filmes =html_raw[1]
#print(top_filmes)
top_filmes.to_html('top.html')