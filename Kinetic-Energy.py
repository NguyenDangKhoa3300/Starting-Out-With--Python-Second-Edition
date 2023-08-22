# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:29:41 2023

@author: mrpot
"""

def main():
    mass = float(input('Enter the mass: '))
    velocity = float(input('Enter the velocity: '))
    print(kinetic_energy(mass, velocity))

def kinetic_energy(mass, velocity):
    ke = 1/2*mass*pow(velocity, 2)
    return ke

main()