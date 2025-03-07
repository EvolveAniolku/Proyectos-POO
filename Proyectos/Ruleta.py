"""
Ruleta de Casino 

INTEGRANTES 
- Juan Pablo Hoyos Chichoque
- Ricardo Farid Cuero Ruiz
- Brayan David Garces Quintero
"""
import random
## Libreria para el uso de numeros aleatorios 

tablero_de_ruleta_color= {
    0: 'Verde',
    1: 'Rojo', 2: 'Negro', 3: 'Rojo',
    4: 'Negro', 5: 'Rojo', 6: 'Negro',
    7: 'Rojo', 8: 'Negro', 9: 'Rojo',
    10: 'Negro', 11: 'Negro', 12: 'Rojo',
    13: 'Negro', 14: 'Rojo', 15: 'Negro',
    16: 'Rojo', 17: 'Negro', 18: 'Rojo',
    19: 'Rojo', 20: 'Negro', 21: 'Rojo',
    22: 'Negro', 23: 'Rojo', 24: 'Negro',
    25: 'Rojo', 26: 'Negro', 27: 'Rojo',
    28: 'Negro', 29: 'Negro', 30: 'Rojo',
    31: 'Negro', 32: 'Negro', 33: 'Negro',
    34: 'Rojo', 35: 'Negro', 36: 'Rojo'
    }
## Seccionamos los colores individualmente los colores
                         
numeros_Max = list(range(0, 37))