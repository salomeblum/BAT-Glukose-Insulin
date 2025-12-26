import numpy as np
from Test_UKF_pyUKF import UKF

def pred_upd_2(data: np.ndarray, pred: np.ndarray,  upd: np.ndarray, estimator: UKF, step: int, start_t: int):
    #data: Für UKF aufbereitete CGM_Daten mit data[0] = Zeit in s, data[1] = CGM-Werte, data[2] = Mahlzeitengrösse in g
    #pred: Array, in dem Vorhersagen von UKF gespeichert werden
    #upd: Array, in dem Updates des UKF gespeichert werden
    #estimator: UKF-estimator
    #step: Prediction-Schritt des UKFs in s, muss ein Teiler von 300 sein
    #start_t: Effektive Startzeit in s (entspricht der Tageszeit, in der der Messdatenpunkt aufgenommen wurde)
    
    t_current = 0 #aktueller Zeitpunkt der Gleichungen (0 bei Start des UKFs)
    data_count = 0
    R = np.array([[0.15]]) #Messrauschen des Sensors
    
    for i in range(0, len(pred)):
        inputs = (t_current, data[:,[0,2]])  #Zeitpunkt der Mahlzeit und Mahlzeitengrösse über den gesamten Schätzzeitraum
        estimator.predict(step, inputs) #Modellvorhersage
        pred[i] = estimator.get_state() #Zustand speichern
        
        while data_count < len(data) and t_current >= data[data_count, 0]:
            cgm = data[data_count, 1] #CGM-Datenwert auslesen für Update-Schritt
            estimator.update([3], cgm, R)
            upd[data_count] = estimator.get_state()
            data_count += 1
    
        t_current += step