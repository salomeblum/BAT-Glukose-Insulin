import numpy as np
from scipy.integrate import odeint

#Solver-Funktion, die es erlaubt Mahlzeit und Mahlzeiten-Zeitpunkt weiterzureichen
#WICHTIG: Das array Dt sollte alle Zeitpunkte t_eval enthalten, zu denen die Simulation ausgeführt werden soll

def f_solve_Dt(func: callable, y0: np.ndarray, Dt: np.ndarray) -> np.ndarray:
    """
    Numerische Integration des ODE-Systems mit LSODA (via odeint).

    func: Funktion, die dx/dt liefert ( rechte Seite des ODE-Systems )
    y0: Startzustand zum Zeitpunkt t_eval[0]
    t_eval: Zeiten, zu denen die Lösung x(t) zurückgegeben werden soll
    D: Input (z.B. Glukosemenge für Magen-Darm-Modell)

    Rückgabe:
    x_of_t : numpy array mit Form (len(t_eval) x len(x0))
             Die simulierten Zustände x(t_eval[i]) für alle Zeitpunkte.
    """
    #Zeitvektor für Solverfunktion
    t_eval = Dt[:,0] #Zeitpunkte, zu denen die Gleichungen gelöst werden sollen
    
    #Mahlzeiten und Mahlzeitenzeitpunkte
    D_mask = Dt[:,1] > 0 
    D_size = Dt[D_mask, 1] #Mahlzeiten, die gegessen wurden
    D_t = Dt[D_mask, 0] #Mahlzeit-Zeitpunkte
    meal_events = list(zip(D_t, D_size))   # [(ti, Di), ...]
    
    sol = odeint(func=func, y0=y0, t=t_eval, args=(meal_events, ))
    return sol
    
    