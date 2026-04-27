from pyscript import display
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
from js import document
import numpy as np
import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

data = [0, 0, 0, 0, 0]


def add_data(event=None):
    selected_day = document.getElementById("day").value
    absences_input = document.getElementById("absences").value
    if absences_input == "":
        return

    absences = int(absences_input)
    index = days.index(selected_day)
    data[index] = absences
    show_graph()


def show_graph():
    plt.clf()
    x = np.arange(len(days))
    plt.plot(x, data, marker='o')

    plt.xticks(x, days)
    plt.title("Weekly Absences")
    display(plt, target="out", append=False)