import numpy as np
import matplotlib.pyplot as plt

def estimate_error(difference:np.ndarray, time:np.ndarray) -> np.ndarray:
    n_cols = difference.shape[1]
    result = np.zeros((4, n_cols))

    for col in range(n_cols):
        RSS = np.sum(difference[:,col]**2) #Residual sum of squares
        RMSE = np.sqrt(1/len(difference)*RSS) #Root mean square error
        MAE = np.mean(np.absolute(difference[:,col])) #Mean absolute error
        bias = np.sum(difference[:,col])/len(difference) #bias
        result[0,col]=RSS #RSS in Zeile 1
        result[1,col]=RMSE #RMSE in Zeile 2
        result[2,col]=MAE #MAE in Zeile 3
        result[3,col]=bias #Bias in Zeile 3

    fig, ax = plt.subplots(2,2, figsize = (12, 8))
    #Überprüfen, wie gross der Unterschied zwischen Simulation und Vorhersage ist
    ax[0,0].plot(time, difference[:,0], label = "M_gut Diff Prediction-Simulation")
    ax[0,0].legend()
    ax[0,1].plot(time, difference[:,1], label = "G_pl Diff Prediction-Simulation")
    ax[0,1].legend()
    ax[1,0].plot(time, difference[:,2], label = "I_pl Diff Prediction-Simulation")
    ax[1,0].legend()
    ax[1,1].plot(time, difference[:,3], label = "G_i Diff Prediction-Simulation")
    ax[1,1].legend()
    plt.tight_layout()

    return result