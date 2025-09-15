import matplotlib
matplotlib.use('Agg')  #'Qt5Agg', 'WebAgg'
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import pandas as pd 
import numpy as np
import mplcursors
import io
import base64

def getCSV(url):
    dfl = pd.read_csv(url)
    return dfl

def draw(filtered_df, c1, c2, c3):
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))

        print(filtered_df["c1"])

        a = ax.plot(filtered_df["c1"]["CensusYear"], filtered_df["c1"]["VALUE"], linestyle="-", linewidth=3.5, color="#A44", label=c1)
        b = ax.plot(filtered_df["c2"]["CensusYear"], filtered_df["c2"]["VALUE"], linestyle="-", linewidth=3.5, color="#4A4", label=c2)
        c = ax.plot(filtered_df["c3"]["CensusYear"], filtered_df["c3"]["VALUE"], linestyle="-", linewidth=3.5, color="#AA4", label=c3)

        title_string = 'Population of counties '+c1+', '+c2+', '+c3+', 1841 - 2022.'

        ax.set_xlabel("Year")
        ax.set_ylabel("Population")
        ax.set_title(title_string)
        ax.set_facecolor('#EEEEEE') 
        ax.legend()
        plt.grid(True, axis="y")

        cursor = mplcursors.cursor(a, hover=True)
        @cursor.connect("add")
        def on_add(axis):
            x_axis, y_axis = axis.target
            axis.annotation.set_text(f"Year: {x_axis:.0f} \nPopulation: {int(y_axis):,d}")
            axis.annotation.get_bbox_patch().set(fc="#66F", alpha=0.6)

        # Save plot to memory buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)

        # Encode the image in base64
        graph_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        buffer.close()
        plt.close(fig)
        return graph_base64

def generateGraph(counties):
    df = getCSV("bogearrai/util/historical.csv")

    filtered_df = df[df['Sex']=="Both sexes"]

    c1, c2, c3 = counties["c1"].capitalize(), counties["c2"].capitalize(), counties["c3"].capitalize()
    c1_df = filtered_df[filtered_df['County']==c1]
    c2_df = filtered_df[filtered_df['County']==c2]
    c3_df = filtered_df[filtered_df['County']==c3]
    df_map = {
        "c1":c1_df,
        "c2":c2_df,
        "c3":c3_df
    }

    #print(df_map)

    graph = draw(df_map, c1, c2, c3)
    return graph
