# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# Librerie:
from itertools import permutations
import random

"""
Ci sono cinque porzioni di eredità: A, B, C, D, E

Devo assegnarle a 5 persone. Devo quindi fare una
permutazione di 5 oggetti. So che ci sono 5! possibilità
diverse. (5! = 120)

Ciascun erede sceglie un numero tra: {1, 2, 3, 4, 5}
Le porzioni di eredità vengono assegnate in ordine:

Esempio:
Viene estratta la combinazione: [B, D, E, A, C]
- al primo erede (numero 1) verrà assegnata B
- al secondo (numero 2) erede verrà assegnata D
...
- al quinto (numero 5) erede verrà assegnata C

L'idea è la seguente:
1. Genero le varie possibilità.

2. Le metto in ordine casuale.

3. Suddivido le possibili combinazioni in gruppi di 4.
    in questo modo avrò 30 gruppi (120/4) ciascuno contenente
    4 possibili allocazioni (tutte diverse ed in ordine casuale).
    Nel contratto scrivo i vari gruppi.

4. Controllo la prima ruota del lotto nazionale (che ha 90 numeri). Per
    scegliere il gruppo vincente adotto la seguente regola:
    ° [1-3] -> primo gruppo
    ° [4-6] -> secondo gruppo
    ° ...
    ° [88-90] -> trentesimo gruppo

    dove [n-k] = "E' uscito un numero compreso tra n e k". Ad esempio:
    [7-9] = {7, 8, 9} (estremi dunque COMPRESI)
    N.B: ogni gruppo ha la stessa probabilità di essere estratto (p = 3/90 = 0.0333)

5. Nel punto 4. ho trovato il gruppo vincente. Adesso devo solo scegliere quale
    delle 4 combinazioni rimanenti scegliere. Guardo alla II e alla III ruota. 
    Il numero vincente di ogni ruota sarà (con ugual probabilità) pari o dispari. 
    Dunque, chiamando "[p,d] = la II ruota è pari, la III è dispari" adotto la seguente
    regola:
    - [p,p] -> prima combinazione
    - [p,d] -> seconda combinazione
    - [d,d] -> terza combinazione
    - [d,p] -> quarta combinazione
    N.B.: all'interno di ogni gruppo ogni combinazione ha la stessa probabilità di essere
    estratta (p = 0.25).

6. Da notare che una combinazione ha la seguente probabilità di essere estratta:
    P = 0.0333*0.25 = 0.008333
    e noto che P*120 = 1
    Questo verifica che ogni combinazione abbia la STESSA probabilità di essere estratta.
"""
# 1. Genero tutte le possibili combinazioni:
porzioni = ['A', 'B', 'C', 'D', 'E']
possibiliCombo = list(permutations(porzioni))
print("Ho ottenuto ", len(possibiliCombo), " combinazioni diverse")

# 2. Dispongo in ordine casuale le combinazioni:
random.shuffle(possibiliCombo)

# 3-I. Suddivido le combinazioni in 30 gruppi di 4 elementi:
gruppi = [[0] * 4 for i in range(30)]
t = 0
for i in range(30):
    for j in range(4):
        gruppi[i][j] = possibiliCombo[t]
        t += 1

# 3-II. Mostro la combinazione e la scrivo sul
# contratto (Cambia sembre la disposizione, basta però
# che ne prenda una e la fissi sul contratto). 
for i in range(30):
    print(i+1, ") ", gruppi[i])

# Aspetto l'uscita del lotto nel giorno prestabilito....vedo la combinazione che esce!

