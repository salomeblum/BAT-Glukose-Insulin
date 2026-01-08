# Daten und Programme zur BAT „Digital Twin zur Modellierung und Interpretation kontinuierlich erfasster Glukosedaten“

Dieses Repository enthält Daten und Programme, die im Rahmen der Bachelorarbeit (BAT) **„Digital Twin zur Modellierung und Interpretation kontinuierlich erfasster Glukosedaten“** entstanden sind.  
Die bereitgestellten Daten und Implementierungen können weiterverwendet werden.

## Repository-Struktur

### Sensordata
Enthält die im Rahmen der Arbeit verwendeten Mess- und Ereignisdaten:

- **CGM.csv**  
  Datei mit kontinuierlichen Glukosemessungen im Zeitraum vom **04.12.2025 bis 14.12.2025**.  
  Vollständige Messtage (00:00–23:59) liegen für den Zeitraum **05.12.2025 bis 13.12.2025** vor.

- **clean_data.csv**
  Datei mit bereinigten Daten, bei denen Zeilen mit NaN-Einträgen (Signal-Verlust des Sensors) entfernt wurden und Spaltenüberschriften angepasst wurden.

- **events.csv**  
  Datei mit zugehörigen Ereignissen (Mahlzeiten und körperliche Aktivitäten) für den Zeitraum **05.12.2025 bis 13.12.2025**.


---

### Matlab
- MATLAB-Implementierung des **E-DES-Modells**
- Zugehörige **Parameterdatei** zur Konfiguration und Simulation des Modells

---

### JupyterLab
Enthält Python-basierte Implementierungen und Analysen:

- **pyUKF**  
  Implementierung eines Unscented Kalman Filters (UKF) (https://github.com/balghane/pyUKF)

- **`f_odes*`**  
  Verschiedene Implementierungen des zugrunde liegenden Gleichungssystems (ODEs)

- **`f_solver*`**  
  Verschiedene Implementierungen numerischer Solver zur Integration des Modells

- **Jupyter Notebooks**  
  Notebooks zur:
  - Analyse der Sensordaten  
  - Durchführung von Zustands- und Parameterschätzungen

---

