import numpy as np
import matplotlib.pyplot as plt

def plot_ukf(sim_data:np.ndarray, ukf_updated: np.ndarray, ukf_predicted: np.ndarray, time_sim: np.ndarray, time_predict: np.ndarray):

    mask = np.isin(time_predict, time_sim)
    ukf_pred_masked = ukf_predicted[mask]
    compare_pred_sim = ukf_pred_masked-sim_data
    compare_pred_upd = ukf_pred_masked-ukf_updated

    fig, ax = plt.subplots(4,2, figsize = (12, 16))
    
    #Magen/Darm: Predicted - Updated - simuliert
    ax[0,0].plot(time_sim, sim_data[:,0], "o", label = "M_gut simulated")
    ax[0,0].plot(time_sim, ukf_updated[:,0], "o", mfc="none", label = "M_gut updated")
    ax[0,0].plot(time_predict, ukf_predicted[:,0], label = "M_gut predicted")
    ax[0,0].legend()
    
    
    #Magen/Darm: Differenz Predicted - updated - simuliert
    ax[0,1].plot(time_sim, compare_pred_upd[:,0], label = "M_gut Predicted - Updated")
    ax[0,1].plot(time_sim, compare_pred_sim[:,0], label = "M_gut Predicted - Simulated")
    ax[0,1].legend()
    
    
    #Glukose Blut-Plasma: Predicted - Updated - simuliert
    ax[1,0].plot(time_sim, sim_data[:,1], "o",  label = "G_pl simulated")
    ax[1,0].plot(time_sim, ukf_updated[:,1], "o", mfc='none', label = "G_pl updated")
    ax[1,0].plot(time_predict, ukf_predicted[:,1], label = "G_pl predicted")
    ax[1,0].legend()
    
    
    #Glukose im Blut-Plasma: Differenz predicted - updated - simuliert
    ax[1,1].plot(time_sim, compare_pred_upd[:,1], label = "G_pl Predicted - Updated")
    ax[1,1].plot(time_sim, compare_pred_sim[:,1], label = "G_pl Predicted - Simulated")
    ax[1,1].legend()
    
    
    #Insulin Blut-Plasma
    ax[2,0].plot(time_sim, sim_data[:,2], "o", label = "I_pl simulated")
    ax[2,0].plot(time_sim, ukf_updated[:,2], "o", mfc='none', label = "I_pl updated")
    ax[2,0].plot(time_predict, ukf_predicted[:,2], label = "I_pl predicted")
    ax[2,0].legend()
    
    
    #Insulin Blut-Plasma: Differenz predicted - updated - simuliert
    ax[2,1].plot(time_sim, compare_pred_upd[:,2], label = "I_pl Predicted - Updated")
    ax[2,1].plot(time_sim, compare_pred_sim[:,2], label = "I_pl Predicted - Simulated")
    ax[2,1].legend()
    
    
    #Glukose Interstitium
    ax[3,0].plot(time_sim, sim_data[:,3], "o", label = "G_i simulated")
    ax[3,0].plot(time_sim, ukf_updated[:,3], "o", mfc='none', label = "G_i updated")
    ax[3,0].plot(time_predict, ukf_predicted[:,3], label = "G_i predicted")
    ax[3,0].legend()
    
    
    #Glukose Interstitium: Differenz predicted - updated - simuliert
    ax[3,1].plot(time_sim, compare_pred_upd[:,3], label = "G_i Predicted - Updated")
    ax[3,1].plot(time_sim, compare_pred_sim[:,3], label = "G_i Predicted - Simulated")
    ax[3,1].legend()
    
    plt.tight_layout()