import numpy as np

#add gene_lengths and exon_counts into two Ndarrays
gene_lengths = np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
exon_counts = np.array([51,1142,42,216,25,650,32533,57,1,523])

#cauculate average exon length, which equal to gene_lengths divide by exon_counts
average_exon_length = gene_lengths/exon_counts

print(average_exon_length)

# Create a figure instance
fig = plt.figure(figsize=(6,5))

# Create an axes instance
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])

# rectangular box plot
labels = ['average exon length']
bplot1 = ax1.boxplot(average_exon_length,
                     vert=True,         # vertical box alignment
                     patch_artist=True, # fill with color
                     labels=labels)     # will be used to label x-ticks
ax1.set_title('average exon length', fontsize=28)

# adding horizontal grid lines
ax1.yaxis.grid(True)

ax1.set_ylabel('length')

f=ax1.boxplot(sym='r*',patch_artist=True)
for box in f['boxes']:
    # Border color
    box.set( color='#7570b3', linewidth=2)
    # Box color
    box.set( facecolor = '#1b9e77' )

plt.show()
