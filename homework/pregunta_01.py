"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    plt.figure()

    colors = {"Television":"dimgray",
            "Newspaper": "grey",
            "Internet": "tab:blue",
            "Radio": "Lightgrey",
            }
    
    zorder = {"Television": 1,
            "Newspaper": 1,
            "Internet": 2,
            "Radio": 1,
            }
    
    linewidths = {"Television": 2,
            "Newspaper": 2,
            "Internet": 4,
            "Radio": 2,
            }

    dfp = pd.read_csv("files/input/news.csv", index_col=0)

    for columnilla in dfp.columns:
        plt.plot(
            dfp[columnilla], 
            color=colors[columnilla],
            label=columnilla,
            zorder=zorder[columnilla],
            linewidth=linewidths[columnilla],
            )

    plt.title("How people get their news", fontsize=16)

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for columnilla in dfp.columns:
        first_year = dfp[columnilla].index[0]
        plt.scatter(
            x=first_year,
            y=dfp[columnilla][first_year],
            color=colors[columnilla],
            zorder=zorder[columnilla],
        )

        plt.text(
            first_year -0.2,
            dfp[columnilla][first_year],
            columnilla + " "+ str(dfp[columnilla][first_year]) + "%",
            ha = "right",
            va = "center",
            color = colors[columnilla],
        )


        last_year = dfp[columnilla].index[-1]
        plt.scatter(
            x=last_year,
            y=dfp[columnilla][last_year],
            color=colors[columnilla],
            zorder=zorder[columnilla],
        )

        plt.text(
            last_year + 0.2,
            dfp[columnilla][last_year],
            str(dfp[columnilla][last_year]) + "%",
            ha = "left",
            va = "center",
            color = colors[columnilla],
        )

    plt.xticks(
        ticks=dfp.index,
        labels=dfp.index,
        ha = "center",
    )
    
    os.makedirs(os.path.dirname("files/plots/news.png"), exist_ok=True)
    plt.savefig("files/plots/news.png")
    plt.show()
    
pregunta_01()