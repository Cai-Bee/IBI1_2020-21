import numpy as np

#add gene_lengths and exon_counts into two Ndarrays
gene_lengths = np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
exon_counts = np.array([51,1142,42,216,25,650,32533,57,1,523])

#cauculate average exon length, which equal to gene_lengths divide by exon_counts
L = gene_lengths/exon_counts
L = L.tolist()
L.sort()
print("list of sorted values for the average exon length across all 10 genes\n",L)

# Create a figure instance
fig = plt.figure(figsize=(6,5))

# Create an axes instance
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])

# rectangular box plot
average_exon_length = L
labels = ['average exon length']
bplot1 = ax1.boxplot(average_exon_length,       #data of boxplot
                     vert=True,         # vertical box alignment
                     patch_artist=True, # fill with color
                     labels=labels)     # will be used to label x-ticks
#set title of ax1
ax1.set_title('average exon length', fontsize=28)

# adding horizontal grid lines
ax1.yaxis.grid(True)

ax1.set_ylabel('length')
plt.show()
