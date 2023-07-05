import matplotlib.pyplot as plt
import numpy as np


def show_repartition(speciation):
    data = {}
    incr = 0
    for key in speciation.keys():
        data[incr] = len(speciation[key])+1
        incr += 1
    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(courses, values, color='mediumvioletred',
            width=0.4, tick_label=values)

    plt.xlabel("Families")
    plt.ylabel("Number of members in the family")
    plt.title("Speciation repartition")
    plt.show()