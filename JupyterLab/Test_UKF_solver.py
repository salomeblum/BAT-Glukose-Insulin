import numpy as np
from scipy.integrate import odeint

#Grundlegende Solver-Funktion, wenn D bei t=0 übergeben wird

def f_solve(func: callable, y0: np.ndarray, t_eval: np.ndarray, D: float) -> np.ndarray:
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
    sol = odeint(func=func, y0=y0, t=t_eval, args=(D,))
    return sol
    
    