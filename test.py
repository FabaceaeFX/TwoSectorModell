import numpy    as np
import networkx as nx
import matplotlib.pyplot as plt 
import matplotlib.cm as cm

networkGraph             = nx.complete_graph(6)
candidate                 = 1
neighbors                 = list(networkGraph.neighbors(candidate))
consumptions              = np.array([0,0,1,0,0,0])
savingsRates              = np.array([7,8,9,10,11,12])
capitalsC                 = np.array([1,0,5,1,1,0])
capitalsF                 = np.array([0,1,0,0,0,1])
incomes                   = np.array([0,1,0,0,0,1])
ones                      = np.ones(len(savingsRates))

cleanIndex                = np.where(capitalsC  != 0)
fossilIndex               = np.where(capitalsF != 0)










# Define numbers of generated data points and bins per axis.
N_numbers = 100000
N_bins = 100

# set random seed 
np.random.seed(0)



# Generate 2D normally distributed numbers.
x, y = np.random.multivariate_normal(
        mean=[0.0, 0.0],      # mean
        cov=[[1.0, 0.4],
             [0.4, 0.25]],    # covariance matrix
        size=N_numbers
        ).T                   # transpose to get columns

print(x, x.shape, y, y.shape)

# Construct 2D histogram from data using the 'plasma' colormap
plt.hist2d(x, y, bins=N_bins, cmap='plasma')

# Plot a colorbar with label.
cb = plt.colorbar()
cb.set_label('Number of entries')

# Add title and labels to plot.
plt.title('Heatmap of 2D normally distributed data points')
plt.xlabel('x axis')
plt.ylabel('y axis')

# Show the plot.
plt.show()





