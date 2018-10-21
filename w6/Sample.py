from random import random

class Sample:
    def __init__(self, max_val):
        self.max_val = max_val
        self.sample_txt = []
        self.n = 0
        self.sorted = False
        
    def sampleInc(self, x):
        self.n += 1
        listSize = len(self.sample_txt)
        
        if listSize < self.max_val:
            self.sorted = False
            self.sample_txt.append(x)
        
        elif random() < (listSize/self.n):
            self.sorted = False
            self.sample_txt[int(random()*listSize)] = x  
        return x
    
    def sampleSorted(self):
        if not self.sorted:
            self.sorted = True
            self.sample_txt.sort()
        
        return self.sample_txt
        
    def nth(self, n):
        s = self.sampleSorted()
        return s[min(len(s), max(1, int(n*len(s))))]     
        
        
    def nths(self, ns = [0.1,0.3,0.5,0.7,0.9]):
        out = list()
        for n in ns:
            out.append(nth(ns))
        
        return out
