from cs50 import get_float, get_string, get_int
from time import sleep
from random import randint, uniform
from helpers import loadingBar, factors, lookup
from helpers import Algometer, Geigometer
from subprocess import call
import donut

UNIV = 12.298
UNICON=0.14

#Oversees and runs all calculations
def main():
    print('1- Archain')
    print('2- Balian')
    print('3- Lookup')
    print('4- Donut')
    ans = get_string('Which of the previous sequences would you like to run?: ')
    ans.lower()
    ans.strip()
    sleep(.5)
    if ans == 'archain' or ans == '1':
        print('Running Archian Calculation')
        sleep(.5)
        inuit = Balian(False)
        sleep(.9)
        print('Calibrating...')
        loadingBar(19, .4)
        sleep(.9)
        rand = randint(1, 20)
        if rand > 2:
            print('Calibration Successful')
            sleep(1.3)
            Archain(inuit)
        else:
            print('Calibration failed, please run again')
    elif ans == 'balian' or ans == '2':
        print('Running Balian Calculation')
        sleep(.5)
        Balian(True)
    elif ans == 'lookup' or ans == '3':
        print('Running error lookup')
        sleep(.5)
        notation = get_string('Enter error notation as given: ')
        notation = notation.lower()
        notation.strip()
        sleep(.5)
        print(lookup(notation))
        sleep(.5)
    elif ans == 'donut' or ans == '4':
        ans2 = get_string('You are about to travel into another universe, do you agree?(Y/N): ')
        ans2.lower()
        ans2.strip()
        if ans2 == 'y' or ans2 == 'yes':
            get_string('Resize your termial to full-screen, hit enter when you are ready')
            call(["python", "donut.py"])
    elif ans == 'ls':
        loadingBar(23, .4)
    else:
        print('Sequence invalid')

def Archain(inuit):
    """
    Calculates smallest basis of time for a specific timeline
    """
    def_alloc = randint(5, 50)

    falliableA = [1.24, 0.98, 3.97, 74.2, 13.8, 12]
    falliableB = {0.98: 'Vr', 1.24: 'S', 3.97: 'ER', 12: 'A9', 13.8: 'cbl2', 47.95:'r9', 74.2:'NaS'}
  
    calc = Algometer
    clr_s = calc.calculate_unit(calc, def_alloc)
    #Linear integrity is in essence how much the base unit of time changes over a certain period of time
    #It is used to determine how accurate the falliability of a calculation is
    spc = get_float('What is the linear integrity of your timeline?: ')
    sleep(1)
    falliability = calc.calculate_falliability(calc, spc, clr_s)
    falliability *= uniform(.15, 1.2)
    notation_key = calc.tappaclan_runner(calc, falliability)
    
    for i in falliableA:  
        if i == notation_key:
            notation_use = True
            break
        else:
            notation_use = False

    #To note- no terminal status estimate is ever comlpletely acurate since it is impossible to completely caulate the base
    #unit of time, so a value of falliability(meaning how much of a difference there can be in the value given)
    #is used to compensate
    if notation_use == True:
        #Most often a variance value is unnreliable, so an error notation is given instead
        print(f'Terminal status is {clr_s}; range of variance unreliable, error notation- [{falliableB[notation_key]}]')
    else:
        print(f'Base unit of terminal status is {clr_s}; adverage range of variance is {round(falliability, 2)}')


def Balian(type):
    """
    Calculates the rate of time at which an object passes
    """
            
    calc = Geigometer
    rad = get_float('Radiation measured in Geigers: ')
    sleep(.5)
    carbon = get_float('Carbon dating Tone ratings: ')
    sleep(.5)
    out1 = calc.calculate_verse(calc, rad, carbon)
    timeline = get_int("Enter timeline representation: ")
    sleep(.5)

    out2 = calc.calculate_continuation(calc, rad, carbon, timeline)

    if out2 < 0:
        out2 = abs(out2)

    if factors(out1, out2):
        print(f'{round(out1, 2)} unical verse(s) parrallel to the {round(out2)}th quantum contiuation')
    else:
        print(f'{round(out1, 2)} unical verse(s) unstable to the ionic quantum contiuations')

    return factors(out1, out2)


if __name__ == '__main__':
    main()