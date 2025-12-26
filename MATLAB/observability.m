%-------------Symbole---------------------------%
syms M_gut G_pl I_pl G_i real %Zustände
syms k1 k2 k3 k4 k5 k6 k7 k8 k9 tau_d tau_i tau_g sigma D_meal g_liv_b G_pl_b I_pl_b f V_G M_b K_M c1 G_pl_th real %Parameter
syms t %Zeit

%-------------Gleichungssystem------------------%

%Magen/Darm-Gleichung
m_G_meal = sigma*(k1^sigma)*t^(sigma-1)*exp(-(k1*t)^sigma)*D_meal;
m_G_pl = k2*M_gut;

dM_gut = m_G_meal - m_G_pl;

%Blut-Plasma-Gleichung
g_liv = g_liv_b - k3*(G_pl - G_pl_b) - k4*(I_pl-I_pl_b);
g_gut = f*k2*M_gut/(V_G*M_b);
g_nonit = ((g_liv_b*(K_M+G_pl_b)/G_pl_b) - I_pl_b*k5)*G_pl/(K_M+G_pl);
g_it = k5*I_pl*G_pl/(K_M+G_pl);
g_ren = 0; %Weil in den meisten Fällen der Glukose-Spiegel die Grenze für die Nierenausscheidung nicht überschreitet. Allfällig Situation bei Hyperglykämie separat betrachten

dG_pl = g_liv + g_gut - g_nonit - g_it - g_ren;

%Insulin im Plasma - Gleichung
i_pnc = k6*(G_pl - G_pl_b) + (k7/tau_i)*G_pl_b + k8*tau_d*dG_pl;
i_liv = k7*G_pl_b/(tau_i*I_pl_b)*I_pl;
i_if = k9*(I_pl-I_pl_b);

dI_pl = i_pnc - i_liv - i_if;

%Glukose im Interstitum Konzentrationsausgleich

dG_i = (1/tau_g)*(G_pl-G_i);


%------------Observability States------------------%
%Zustandsvektor
x = [M_gut;
    G_pl;
    I_pl;
    G_i];

%Funktionsvektor
f= [dM_gut;
    dG_pl;
    dI_pl;
    dG_i];

%Matrix A
A_states = jacobian(f,x);
A_states_s = simplify(A);
A_states


%Matrix C
h = G_i;
C_states = jacobian(h,x);

%Observability
O_states = [C_states;
    C_states*A_states;
    C_states*A_states*A_states;
    C_states*A_states*A_states*A_states];

O_states

rank(O_states)


%-------------Observability States & Params-------------%
%Vektor erweitert
x_erw = [M_gut;
    G_pl;
    I_pl;
    G_i;
    k1;
    k5;
    tau_g];

%Funktionsvektor erweitert
f_erw = [dM_gut;
    dG_pl;
    dI_pl;
    dG_i;
    0;
    0;
    0];

%Matrix A
A_erw = jacobian(f_erw,x_erw);
A_erw_s = simplify(A_erw);
A_erw_s


%Matrix C
h_erw = G_i;
C_erw = jacobian(h_erw,x_erw);

%Observability
O_erw = [C_erw;
    C_erw*A_erw;
    C_erw*A_erw^2;
    C_erw*A_erw^3;
    C_erw*A_erw^4;
    C_erw*A_erw^5;
    C_erw*A_erw^6];

O_erw

rank(O_erw)


%------------Vergleich Lie-Derivatives------------%

Lfh = C_erw*f_erw;
C2 = jacobian(Lfh, x_erw);
Lfh2 = C2*f_erw;
C3 = jacobian(Lfh2, x_erw);
Lfh3 = C3*f_erw;
C4 = jacobian(Lfh3, x_erw);
Lfh4 = C4*f_erw;
C5 = jacobian(Lfh4, x_erw);
Lfh5 = C5*f_erw;
C6 = jacobian(Lfh5, x_erw);
Lfh6 = C6*f_erw;
C7 = jacobian(Lfh6,x_erw);

O_Lf = [C_erw;
    C2;
    C3;
    C4;
    C5;
    C6;
    C7];

O_Lf
rank(O_Lf)

% Indizes der Parameter-Spalten:
param_cols = [4 5 6];

% Extrahiere Parameter-Spalten
OP = O_Lf(:, param_cols);

rank_OP = rank(OP)