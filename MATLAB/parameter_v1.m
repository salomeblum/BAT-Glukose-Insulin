% Parameter Modell Glukose-Insulin V.1
% E-DES
% Simulation einer Mahlzeit

%-------------------------------------------------------------------------
% Der Literatur entnommene Werte

sigma = 1.35; %[--] Form-Faktor der Glukoseaufnahme im Magen
beta = 1; %[(mmol/L)/(mU/L)] Konversionsfaktor Glukose --> Insulin
f =  0.005551; %[mmol/mg] Konversionsfaktor mmol --> mg Glukose
V_g =  17/70; %[L/kg] Verteilungsvolumen Glukose im Blutplasma
K_M =  0.63; %[mmol/L] Michaelis-Menten-Konstante für Glukose-Aufnahme
c1 =  0.1/60; %[1/s] Glomeruläre Filtrationsrate

k2 = 6.33e-1/60; %[1/s] Magen-Entleerungsrate 
k3 = 5.00e-5/60; %[1/s] Unterdrückungs-Rate der EGP, wenn G_pl > G_pl_b
k4 = 1.00e-3/60; %[1/s] Insulin-abhängige Unterdrückungs-Rate von EGP
k5 = 3.80e-3/60; %[1/s] Insulin-abhängige Glukose-Aufnahme-Rate
k6 = 5.82e-1/60; %[1/s] Insulin-Produktionsrate, abhängig von (G_pl-G_pl_b)
k7 = 1.15/60; %[1/s] Insulin-Produktionsrate, abhängig von zeitlich integrierter Glukosekonzentration
k8 = 4.71/60; %[1/s] Insulin-Produktionsrate, abhängig von der zeitlichen Änderung der Glukosekonzentration
k9 =  1.08e-2/60; %[1/s] Flussrate des Insulins von Plasma --> Interstitium


G_pl_th = 9; %[mmol/L] Schwellenwert Nierenausscheidung
I_pl_b = 6.5; %[mU/L] --> entnommen aus der Literatur, Modell hat Drift oder irgendetwas Komisches!!

tau_i = 31*60; %[s] Integrations-Zeitkonstante (Glukosekonzentration)
tau_d = 3*60; %[s] Ableitungszeitkonstante (Glukosekonzentration)


%-------------------------------------------------------------------------
% Messwerte
M_b = 75; %[kg] Körpergewicht

%-------------------------------------------------------------------------
% Individuell anzupassende Werte
% Start mit Literatur-Wert, später anpassen

k1 = 1.35e-2/60; %[1/s] Glukose-Aufnahmerate 
g_liv_b = 0.043/60; %[mmol/L/s] Basale endogene Glukoseproduktionsrate (EGP) der Leber
tau_g = 2.5*60; %[s] Ausgleichs-Zeitkonstante zwischen Plasma und Interstitium
G_pl_b = 4.93; %[mmol/L] Literatur-Wert gemäss Erlandsen et al. (2018)

