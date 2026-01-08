import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def estimate_error_2(difference:np.ndarray, diff_tss: np.ndarray, time:np.ndarray, names: list) -> np.ndarray:
    """
    difference: enthält die Differenz der realen Werte zum vorhergesagten Wert
    diff_tss: enthält die Differenz der realen Werte zum Mittelwert der realen Werte --> für TSS
    time: Zeitreihe zum Plotten der Differenz zwischen Vorhersage und realen Daten
    names: Enthält die Beschriftungen zum Plotten der Differenz zwischen Vorhersage und realen Daten"""
    
    n_cols = difference.shape[1]
    result = np.zeros((n_cols, 6))

    for col in range(n_cols):
        RSS = np.sum(difference[:,col]**2) #Residual sum of squares
        RMSE = np.sqrt(1/len(difference)*RSS) #Root mean square error
        MAE = np.mean(np.absolute(difference[:,col])) #Mean absolute error
        bias = np.sum(difference[:,col])/len(difference) #bias
        TSS = np.sum(diff_tss**2) #Total sum of squares
        Rsq = 1-RSS/TSS
        result[col,0]=RMSE #RSS in Spalte 1
        result[col,1]=MAE #RMSE in Spalte 2
        result[col,2]=bias #MAE in Spalte 3
        result[col,3]=RSS #Bias in Spalte 4
        result[col,4]=TSS #TSS in Spalte 5
        result[col,5]=Rsq #R squared in Spalte 6

    fig, ax = plt.subplots(n_cols,1, figsize = (12, 2.5*n_cols))
    
    if n_cols == 1:
        ax = [ax]
    #Plotten, wie gross der Unterschied zwischen Simulation und Vorhersage ist
    for i in range(n_cols):
        ax[i].plot(time, difference[:,i], label = f"{names[i]} Diff Prediction-Real")
        ax[i].legend()
    
    plt.tight_layout()

    result = pd.DataFrame(result, columns = ["RMSE", "MAE", "bias", "RSS", "TSS", "Rsq"], index = names)
    return result