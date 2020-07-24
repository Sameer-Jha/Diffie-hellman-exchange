#!/usr/bin/env python3
q = 77 
a = 29

def key_creator(p1,p2):
    print('Private Key for p1: '+str(p1))
    Ya = pow(a,p1,q)
    print('Private Key for p2: '+str(p2))
    Yb = pow(a,p2,q)

    Ka = pow(Yb, p1, q)
    Kb = pow(Ya, p2, q)

    print(f'Secret Key for Alice is: {Ka}')
    print(f'Secret Key for Bob is: {Kb}')

if __name__ == "__main__":
    key_creator(4,3)