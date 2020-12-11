import numpy as np
import time
from scipy.stats import pearsonr
 
def euclidean(x, y): # x and y being two numpy arrays
    return np.sqrt(np.sum((x-y)**2))

def manhattan(x,y):
    return np.sum(np.abs(x-y))
    
def correlation(x, y):
    return 1.0 - pearsonr(x,y)[0]

class KMeans(object):
    def __init__(self, k):
        """
        Creating model object
        
        Parameters
        ----------
        int k
            number of clusters specified when creating the model object
        """
    
        self.k = k
        
    def fit(self, data=None, distance=None, nruns=10, randomseed=None, verbose=False):
        """
        Fitting k means using EM algorithm.

        Parameters
        ----------
        numpy array data
            of dimension (n,d) where n is sample size and d is the dimension
        distance
            can be "euclidean", "manhattan", "correlation" or user-specified
        int nruns
            number of runs with different initializations, results with lowest cost will be returned
        int randomseed
            random seed
        
        Returns
        -------
        numpy ndarray
            the k centroids, of shape (# ROIs, # ROIs, k)
        numpy array
            the vector of assignments of each data point to clusters
        double
            inertia
        """

        if not randomseed:
            np.random.seed(int(time.time())
        else:
            np.random.seed(int(randomseed))
            
        n = data.shape[0]  # number of FC frames

        inertia = 100000000
        centroids = data[np.random.choice(n,self.k,replace=False),:]  # randomly initialize centroids
        assignment = np.random.choice(self.k, n, replace=True)  # randomly initialize assignments

        for i in range(nruns):
            # Initialization
            centroids_temp = data[np.random.choice(n,self.k,replace=False),:]  # initialize by sampling from data
            assignment_temp = np.random.choice(self.k, n, replace=True)  # initial assignement vector
            niter = 0  # number of iterations
            # Iteration till convergence
            while (niter==0) or (not np.array_equal(assignment_temp, assignment_pre)):
                assignment_pre = assignment_temp.copy()
                # E step
                for sample in range(n):  # go through samples
                    cost = 10000.0
                    for clust in range(k):  # for each sample, compute its distance to each cluster centroid
                        cost_temp = distance(data[sample,:], centroids_temp[clust,:])
                        if cost_temp < cost:
                            assignment_temp[sample] = clust
                            cost = cost_temp
                # M step
                for clust in range(self.k):  # update centroids
                    centroids_temp[clust,:] = np.mean(data[assignment_temp==clust,:], axis=0)

                niter += 1
                if verbose: print("{} iterations completed.".format(niter))
                
        # compute the inertia
        inertia_temp = 0.0
        for sample in range(n):
            inertia_temp = inertia_temp + distance(data[sample,:], centroids_temp[assignment_temp[sample],:])
        
        # keep the results with lowest inertia
        if inertia_temp < inertia:
            inertia = inertia_temp
            assignment = assignment_temp
            centroids = centroids_temp


        return centroids, assignment, inertia
