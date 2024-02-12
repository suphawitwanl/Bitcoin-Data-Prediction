import pickle
import matplotlib.pyplot as plt

# Load the figure
with open('figure_all.pkl', 'rb') as file:
    fig = pickle.load(file)

plt.show()

