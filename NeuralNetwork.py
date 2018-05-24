# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:00:51 2018

@author: Marteaufou
"""

import numpy
import os

class Neural:
    def __init__(self, path):
        
        #Largeur Matrice
        self.TailleEntree = 2
        self.TailleCache = 3
        self.TailleSortie = 1
        
        #Poids
        (self.P1, self.P2) = self.load(path)
        return
        
    def forward(self, E):
        self.T1 = numpy.dot(E, self.W1)
        self.N1 = self.sigmoide(self.T1)
        self.T2 = numpy.dot(self.N1, self.P2)
        return self.sigmoide(self.T2)
        
    def sigmoide(self, P):
        return (1/(1 + numpy.exp(-P)))
        
    def SigmoidePrime(self, P):
        return numpy.exp(-P)/((1+numpy.exp(-P))**2)
        
    def FonctionCoutPrime(self, E, R):
        self.rChap = self.forward(E)
        delta3 = numpy.multiply(-(R-self.rChap), self.SigmoidePrime(self.T2))
        dJdW2 = numpy.dot(self.N1.T, delta3)
        
        delta2 = numpy.dot(delta3, self.P2.T) * self.SigmoidePrime(self.N1)
        dJdW1 = numpy.dot = numpy.dot(E.T, delta2)
        
        return dJdW2, dJdW1
    
    def save(self, path):
        result = ""
        for i in range(0, self.TailleEntree):
            for j in range(0, self.TailleCache):
                result = result + str(self.P1[i][j])
                if (j != (self.TailleCache - 1)):
                    result = result + " "
            if (i != (self.TailleEntree - 1)):
                result = result + ";"
        result = result + "\n"
        
        for i in range(0, self.TailleCache):
            for j in range(0, self.TailleSortie):
                result = result + str(self.P2[i][j])
                if (j != (self.TailleSortie - 1)):
                    result = result + " "
            if (i != (self.TailleCache - 1)):
                result = result + ";"
        result = result + "\0"
        file = open(path, 'w')
        file.write(result)
        file.close()
        return
    
    def load(self, path):
        if (os.path.isfile(path)):
           file = open(path, 'r')
           
           line = file.readline()
           P1 = numpy.matrix(line)
                   
           line = file.readline()
           P2 = numpy.matrix(line)
           
           file.close()
        else:
            P1 = numpy.random.randn(self.TailleEntree, self.TailleCache)
            P2 = numpy.random.randn(self.TailleCache, self.TailleSortie)
        return (P1, P2)

"""        
    def creatematrix(self, string):
        i = 0
        j = 0
        k = 0
        while (string[i] != '\n' and string[i] != '\0'):
            tempstr = ""
            while (string[i] != ';' and string[i] != ' ' and string[i] != '\n' and string[i] != '\0'):
                tempstr = tempstr + string[i]
                i = i + 1
            tempflt = float(tempstr)
            if (string[i] == ' '):
                matrix[k][j] = tempflt
                j += 1
            i = i + 1
        return matrix
"""

def main():
    print("test")
    path = "NeuralNetworkPresentation.txt"
    
    neuralnet = Neural(path)
    
    print("test2")
    
    print(neuralnet.P1)
    print(neuralnet.P2)
    neuralnet.save(path)
        
main()