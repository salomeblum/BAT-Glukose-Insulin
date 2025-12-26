import numpy as np
from Test_UKF_pyUKF import UKF

def pred_upd(pred_data: np.ndarray, sim_data: np.ndarray, upd_data: np.ndarray, mealtime: np.ndarray, estimator: UKF, step: int):
    #Schätzen der 4 Zustände und eines Parameters
    t_current = 1
    data_count = 0
    R = np.array([[0.2]])
    
    for i in range(0, len(pred_data)):
        inputs = (t_current, mealtime)  #Zeitpunkt der Mahlzeit und Mahlzeitengrösse in tuple speichern
        estimator.predict(step, inputs) #Modellvorhersage
        pred_data[i] = estimator.get_state() #Zustand speichern
        
        if t_current == sim_data[data_count,0]:
            cgm = sim_data[data_count, 1] #CGM-Daten auslesen
            estimator.update([3], cgm, R)
            upd_data[data_count] = estimator.get_state()
            data_count += 1
    
        t_current += step