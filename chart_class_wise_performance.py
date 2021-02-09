import csv
import pandas
import matplotlib.pyplot as plt
from loadPreProc import *
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches
from numpy import arange

textDF=pandas.read_csv('tsc_files/classwise_performance.csv')
Categories = ["%d. %s" % (i+1,textDF['label'][i]) for i in range(23)]

fig, ax = plt.subplots(figsize=(10,5)) ##pink, orange
textDF['best_baseline_F score'].plot.bar(width=0.3,  ylim=[0.1, 0.9], xlim=[1,23], position=2.0, color="lightgreen", ax=ax, alpha=1)
textDF['best_proposed_F score'].plot.bar(width=0.3, position=1.0, ylim=[0, 0.9], xlim=[1,23],color="green", ax=ax, alpha=1)
ax.set_facecolor("white")
ax.set_xticklabels(range(1,24), rotation=0, fontsize=10)
ax.set_yticklabels([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],rotation=0, fontsize=10)
ax.set_xlabel("Label IDs",fontsize=10)

best_base = mpatches.Patch(color='lightgreen', label='F score for the best baseline')
best_proposed = mpatches.Patch(color='green', label='F score for our best method')
legend = plt.legend(handles=[best_base,best_proposed],loc="upper right", prop={'size': 10},bbox_to_anchor=(1.0035,1.007))
extra = Rectangle((0, 0), 0.5, 0.5, fc="w", fill=False, linewidth=0)
legend1 = plt.legend([extra]*(len(textDF['label'])), Categories, loc = (1,1), fontsize='small', framealpha=0, handlelength=0, handletextpad=0, prop={'size': 8.4},bbox_to_anchor=(1.017,-0.010))
plt.gca().add_artist(legend)
plt.gca().add_artist(legend1)
plt.savefig('class_wise_performance.pdf',bbox_extra_artists=(ax,), bbox_inches='tight')


