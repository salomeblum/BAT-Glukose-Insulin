import numpy as np
import Test_UKF_params as param

#Gleichungen E-DES-Modell 
#Entspricht dem Input-Format von pyUKF
#erlaubt Mahlzeitinputs zu verschiedenen Zeitpunkten
#erlaubt Erweiterung des UKFs auf Parameterschätzung mit tangens Reparametrisierung
#Ausgabe: dM_gut, dG_pl, dI_pl, dG_i

def f_odes_Dt_tan(x: np.ndarray, t: float, D_t : np.ndarray) -> np.ndarray:
    """
    Rechte Seite des ODE-Systems (EDES-Modell)
    x: Zustandsvektor (numpy array)
    t: Zeit
    D_t: Mahlzeit-Zeitpunkt und Mahlzeit-Grösse
    return: dx/dt als numpy array
    """

    #Beispiel: Zustände extrahieren
    M_gut = x[0]
    G_pl = x[1]
    I_pl = x[2]
    G_i  = x[3]

    #Reparametrisierung k1 mit Tangens
    p_k1 = x[4] #von UKF geschätzer Parameter
    a_k1, b_k1 = 1e-7/60, 3e-1/60 #lower und upper bound für Parameter k1
    k1_t = (a_k1 + b_k1)/2 + (b_k1 - a_k1)/np.pi*np.arctan(p_k1)

    #k5 und tau_g werden als Differenz zum Literaturwert angegeben 
    k5_t = param.k5 + x[5]
    tau_g_t = param.tau_g + x[6]

    #Flüsse Magen
    m_meal = 0.0

    for ti, Di in D_t: #Aufsummieren Mahlzeiteninput zum Zeitpunkt "time"
        if t > ti:
            delta_t = t - ti
            m_meal += param.sigma * (k1_t**param.sigma) * ((delta_t)**(param.sigma-1))*np.exp(-((k1_t*(delta_t))**param.sigma))*Di #Glukose-Aufnahme Magen
    
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
    dG_i   = (G_pl - G_i) / tau_g_t

    return np.array([dM_gut, dG_pl, dI_pl, dG_i, 0.0, 0.0, 0.0])
    
