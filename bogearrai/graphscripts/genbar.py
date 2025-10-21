import matplotlib
matplotlib.use('Agg')  #'Qt5Agg', 'WebAgg'
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import pandas as pd 
import numpy as np
import io
import base64

def getCSV(url):
    dfl = pd.read_csv(url)
    return dfl

def draw(filtered_df, year, c1, c2, c3):
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))

    a = ax.bar(filtered_df["c1"]["County"], filtered_df["c1"]["VALUE"], color="#A44", label=c1)

    title_string = 'Population of counties '+c1+', '+c2+', '+c3+', in '+ str(year)+"."

    ax.set_xlabel("Population", fontsize=16)
    ax.set_ylabel("County", fontsize=16)
    ax.set_title(title_string, fontsize=14)
    ax.set_facecolor('#EEEEEE') 
    ax.legend()
    plt.grid(True, axis="y")

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    graph_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    buffer.close()
    plt.close(fig)
    return graph_base64

def generateGraph(year, c1, c2, c3):
    df = getCSV("bogearrai/util/historical.csv")
    print("H")
    filtered_df = df[df['Sex']=="Both sexes"]

    # c1, c2, c3 = counties["c1"].capitalize(), counties["c2"].capitalize(), counties["c3"].capitalize()
    c1_df = filtered_df[filtered_df['CensusYear']==year]
    c1_df = c1_df[(c1_df['County']==c1)|(c1_df['County']==c2)|(c1_df['County']==c3)]
    df_map = {
        "c1":c1_df
    }

    graph = draw(df_map, year, c1, c2, c3)

    pop_map = {}
    for county, df in df_map.items():
        year = df['CensusYear'].tolist()
        pop = df['VALUE'].tolist()
        list_pop = list(zip(year, pop))
        pop_map[county] = list_pop
        
    return graph, pop_map

generateGraph(2022, "Cork", "Kilkenny", "Waterford")
