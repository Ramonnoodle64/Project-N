from time import sleep
from random import randint, uniform
from cs50 import get_float

UNIV = 12.298
UNICON = 0.14

def loadingScreen(length, time):
    block = '\N{FULL BLOCK}'
    line = '\N{BOX DRAWINGS HEAVY VERTICAL}'
    percentage = 0
    counter = 0
    for i in range(length + 1):
        percentage = "{:.0%}". format(counter/length)
        print('\r' + line, end='')
        print(block, end='')
        for j in range(counter):
            print(block, end='')
        for j in range(length - counter):
            print(' ', end='')
        print(line, end='')
        print('  ' + percentage + " Complete", end='')
        counter += 1
        sleep(time*uniform(0.6, 2.5))
    print('')

def factors(out1, out2):
    diff = out1 - out2
    if diff > UNIV*1.6 or abs(diff) > UNIV*1.6:
        return False
    else: 
        return True

def lookup(notation):
    notation_dictionary = {
        'vr': 'Vr - Falliablility is low, value given is accurate; (Variance report)',
        's': 'S - Falliablility is low, Contents 1-7 Delta-Corrino are stable; (Salem)',
        'er': 'ER - Falliability is moderate, value given may differ; (Emergent Report)',
        'a9': 'A9 - Falliability is high, Contents 8-15 Alpha-Corrino are semi-stable; (Arcen 9)',
        'cbl2': 'cbl2 - Falliability is high, value given will differ (cosantla beros langatiem 20190)',
        'nas': 'NaS - Falliability is immense, value given is inaccurate (Non-acumulative, Supercede standard protocol)',
        'r9': 'R9 - Falliability is over-immense, all Contents of Sigma-Corrino are unstable, area unsafe, evacuate immediately(Report 9)',
    } 
    for i in notation_dictionary.keys():
        if (i == notation):
            return notation_dictionary[notation]
    return 'Notation invalid'

falliableA = [1.24, 0.98, 3.97, 74.2, 13.8, 12]

class Algometer:
        """
        The calculations used to determine the smallest unit of time
        """
        def __init__(self, falliablility, integrity, CLR_K):
            self.falliablility = falliablility
            self.integrity = integrity
            self.CLR_K = CLR_K
        
        def calculate_unit(self, CLR_K):
            #Calculates the Cemi Lateral Raical note K (Note K is the 12th factor basis of time)
            clr_s = UNICON * CLR_K
            clr_s += clr_s**2
            return round(clr_s*10, 3)
        def calculate_falliability(self, spc, CLR_S):
            #Finds the the range of variance possible for CLR_K
            #The Cemi Lateral Radical note S (The inverse factor of note K) is found
            spc *= abs(CLR_S - UNICON)
            return round(spc, 2)
        def tappaclan_runner(self, falliability):
            #The tappaclan runner uses the CLR_S value of variance to find the genral specifications 
            #of a certain timeline
            clr_a = round(falliability)
            for i in falliableA:
                if clr_a < i + i * 1.2:
                    key = i
                    return i
            return None

class Geigometer:
        """
        The calculations required to determine an objects rate of flow through time
        """
        def __init__(self, radiation, carbon):
            self.radiation = radiation
            self.carbon = carbon
        #The calculations used for a Balian calculation
        if type == True:
            def calculate_verse (self, radiation, carbon):
                const = get_float('Enter universal constant for local constelation: ')
                output = radiation + (carbon * radiation/const)
                output = 14.131 - (output/2)
                return(output)

            def calculate_continuation (self, radiation, carbon, timeline):
                if timeline > round(UNIV, 1):
                    allocation = carbon**(timeline/UNIV)
                else:
                    allocation = carbon + UNIV/3
                return(allocation)
        else:
            #Simplified calculations used for an Archain calculation
            #Calculate verse finds the unical verse(The quantum timeline that an object shares a rate of passing time with)
            #of an object using the measured radiation and second class carbon dating
            def calculate_verse (self, radiation, carbon):
                output = radiation + (carbon * radiation)
                output = 4.131 + (output/23)
                return(output)
            #Calculate continuation finds the overflow quantum continuation that a specific timeline follows
            def calculate_continuation (self, radiation, carbon, timeline):
                if timeline > round(UNIV, 1):
                    allocation = carbon**(timeline/UNIV)
                else:
                    allocation = carbon + UNIV/3
                return(allocation)