import numpy as np
import matplotlib.pyplot as plt

def plot_ukf_2(cgm_data:np.ndarray, upd: np.ndarray, pred: np.ndarray, time: np.ndarray, time_pred: np.ndarray):
    #cgm_data: Reale CGM-Daten
    #upd: UKF updates
    #pred: UKF predictions
    #time: Zeitstempel der reellen Daten (in s)
    #time_pred: Zeitstempel der vorhergesagten Daten
    

    mask = np.isin(time_pred, time)
    pred_masked = pred[mask]
    compare_pred = pred_masked[:,3]-cgm_data #Differenz der CGM-Daten real vs. predicted
    compare_pred_upd = pred_masked-upd #Differenz zwischen Vorhersage und Update aller im UKF gehaltenen Zustände
   
    fig, ax = plt.subplots(1,2, figsize = (12, 2.5))
    
    #Glukose im Interstitium: Real versus predicted
    ax[0].plot(time, cgm_data, "o", label = "G_i real")
    ax[0].plot(time_pred, pred[:,3], label = "G_i predicted")
    ax[0].legend()
    
    
    ##Glukose im Interstitium: Differenz Predicted - Updated/Real
    ax[1].plot(time, compare_pred_upd[:,3], label = "G_i Predicted - Updated")
    ax[1].plot(time, compare_pred, label = "G_i Predicted - real")
    ax[1].legend()


    fig, ax = plt.subplots(4,1, figsize = (12, 12))
    
    #Magen/Darm: Predicted - Updated
    ax[0].plot(time, upd[:,0], "o", mfc="none", label = "M_gut updated")
    ax[0].plot(time_pred, pred[:,0], label = "M_gut predicted")
    ax[0].legend()
    
    
    #Glukose Blut-Plasma: Predicted - Updated
    ax[1].plot(time, upd[:,1], "o", mfc='none', label = "G_pl updated")
    ax[1].plot(time_pred, pred[:,1], label = "G_pl predicted")
    ax[1].legend()
    
    
    #Insulin Blut-Plasma
    ax[2].plot(time, upd[:,2], "o", mfc='none', label = "I_pl updated")
    ax[2].plot(time_pred, pred[:,2], label = "I_pl predicted")
    ax[2].legend()
    
    
    #Glukose Interstitium
    ax[3].plot(time, cgm_data, "o", label = "G_i real")
    ax[3].plot(time, upd[:,3], "o", mfc='none', label = "G_i updated")
    ax[3].plot(time_pred, pred[:,3], label = "G_i predicted")
    ax[3].legend()
    
    
    """fig, ax = plt.subplots(4,2, figsize = (12, 16))
    
    #Magen/Darm: Predicted - Updated
    ax[0,0].plot(time, upd[:,0], "o", mfc="none", label = "M_gut updated")
    ax[0,0].plot(time_pred, pred[:,0], label = "M_gut predicted")
    ax[0,0].legend()
    
    #Magen/Darm: Differenz Predicted - updated
    ax[0,1].plot(time, compare_pred_upd[:,0], label = "M_gut Predicted - Updated")
    ax[0,1].legend()
    
    
    #Glukose Blut-Plasma: Predicted - Updated
    ax[1,0].plot(time, upd[:,1], "o", mfc='none', label = "G_pl updated")
    ax[1,0].plot(time_pred, pred[:,1], label = "G_pl predicted")
    ax[1,0].legend()
    
    #Glukose im Blut-Plasma: Differenz predicted - updated
    ax[1,1].plot(time, compare_pred_upd[:,1], label = "G_pl Predicted - Updated")
    ax[1,1].legend()
    
    
    #Insulin Blut-Plasma
    ax[2,0].plot(time, upd[:,2], "o", mfc='none', label = "I_pl updated")
    ax[2,0].plot(time_pred, pred[:,2], label = "I_pl predicted")
    ax[2,0].legend()
    
    
    #Insulin Blut-Plasma: Differenz predicted - updated
    ax[2,1].plot(time, compare_pred_upd[:,2], label = "I_pl Predicted - Updated")
    ax[2,1].legend()
    
    
    #Glukose Interstitium
    ax[3,0].plot(time, cgm_data, "o", label = "G_i real")
    ax[3,0].plot(time, upd[:,3], "o", mfc='none', label = "G_i updated")
    ax[3,0].plot(time_pred, pred[:,3], label = "G_i predicted")
    ax[3,0].legend()
    
    
    #Glukose Interstitium: Differenz predicted - updated - simuliert
    ax[3,1].plot(time, compare_pred_upd[:,3], label = "G_i Predicted - Updated")
    ax[3,1].plot(time, compare_pred, label = "G_i Predicted - Real")
    ax[3,1].legend()"""
    
    plt.tight_layout()