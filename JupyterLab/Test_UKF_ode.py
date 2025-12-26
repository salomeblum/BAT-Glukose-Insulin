import numpy as np
import Test_UKF_params as param

#Modellgleichungen E-DES
#Mahlzeiteninput zum Zeitpunkt t=0
#Verwendet Literaturwerte für Parameter
#Ausgabe dM_gut, dG_pl, dI_pl, dG_i

def f_odes(x: np.ndarray, t: float, D: int) -> np.ndarray:
    """
    Rechte Seite des ODE-Systems (EDES-Modell)
    x: Zustandsvektor (numpy array)
    t: Zeit
    u: Input (z.B. Mahlzeiten)
    return: dx/dt als numpy array
    """

    # Beispiel: Zustände extrahieren
    M_gut = x[0]
    G_pl = x[1]
    I_pl = x[2]
    G_i  = x[3]

    # Parameter (Literaturwerte)
    k1_t = param.k1
    k5_t = param.k5
    tau_g_t = param.tau_g
    

    #Flüsse Magen
    m_meal = param.sigma * (k1_t**param.sigma) * (t**(param.sigma-1))*np.exp(-((k1_t*t)**param.sigma))*D #Glukose-Aufnahme Magen
    m_pl = param.k2*M_gut #Glukose-Abgabe ans Blutplasma
    
    #Magen/Darm-Gleichung
    dM_gut = m_meal - m_pl
    
    #Flüsse Plasma-Glukose
    c2 = param.g_liv_b*((param.K_M+param.G_pl_b)/param.G_pl_b)-param.I_pl_b*k5_t*param.beta #Hilfskonstante zur Berechnung von g_non_it
    
    g_liv = param.g_liv_b - param.k3*(G_pl - param.G_pl_b) - param.k4*param.beta*(I_pl - param.I_pl_b)
    g_gut = param.f*m_meal/(param.V_g*param.M_b)
    g_non_it = c2*(G_pl/(param.K_M+G_pl))
    g_it = k5_t*param.beta*I_pl*G_pl/(param.K_M+G_pl)

    if G_pl > param.G_pl_th:
        g_ren = param.c1*(G_pl-param.G_pl_th)/(param.V_g*param.M_b)
    else:
        g_ren = 0

    #Plasma-Glukose-Gleichung
    dG_pl  = g_liv + g_gut - g_non_it - g_it - g_ren
    

    #Flüsse Plasma-Insulin
    i_pnc = 1/param.beta*(param.k6*(G_pl-param.G_pl_b) + (param.k7/param.tau_i)*param.G_pl_b + (param.k8*param.tau_d)*dG_pl)
    i_liv = param.k7*param.G_pl_b/(param.beta*param.tau_i*param.I_pl_b)*I_pl
    i_if = param.k9*(I_pl-param.I_pl_b)
    
    #Plasma-Insulin-Gleichung
    dI_pl  = i_pnc - i_liv - i_if

    
    #Glukose im Interstitium - Gleichung
    dG_i   = (G_pl - G_i) / param.tau_g

    return np.array([dM_gut, dG_pl, dI_pl, dG_i])
    

if __name__ == "__main__":
    #Nur für Debugging - gibt Daten mit konstantem Zustand heraus - keine Modellsimulation
    print("Test starte...")
    dt = 300
    G_start = param.G_pl_b
    I_start = param.I_pl_b
    x = np.array([0,G_start,I_start,G_start])
    
    for t in np.arange(1, 86400, dt):
        dxdt = f_odes(x, t, 75000)
        print(dxdt)
    