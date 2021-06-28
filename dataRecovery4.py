#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 21:25:00 2021

@author: shrohanmohapatra
"""
### Thanks to https://stackoverflow.com/questions/3160699/python-progress-bar
import mph
import sys
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
client = mph.start(cores=1)
model = client.load('2DGeometryExample.mph')
print(model.parameters())
print('Start of the simulation')
ReList = [10**(-5),10**(-4),10**(-3),10**(-2),10**(-1)]
fileHandle = open('dataStorageFile.txt','w')
try:
    for Re in progressbar(ReList,"Progress 1: ",40):
        r0List = [(5.26*k-5.16)*Re for k in range(1,21)]
        for r0 in progressbar(r0List,"Progress 2: ",40):
            model.parameter('Re',str(Re))
            model.parameter('r0',str(r0)+'[m]')
            try:
                model.solve()
            except:
                pass
            try:
                result = model.evaluate('integrate(subst(abs(comp1.vy)*Re/rho/a,y,0),x,r0,2*a-r0)')
            except:
                pass
            result1 = sum(result.tolist())
            try:
                result = model.evaluate(
                    'integrate(subst(abs(comp1.ux*(x-r0)^2/r0^2+mu*comp1.vy*(y-r0)^2/r0^2+mu*(comp1.uy+comp1.vx)*(x-r0)*(y-r0)/r0^2)*Re/rho/a,y,r0-sqrt(2*r0*x-x^2)),x,0,r0)'
                    )
            except:
                pass
            result2 = sum(result.tolist())
            print('Re='+str(Re)+' r0/a='+str(r0)+' F/mu/U='+str(4*(result1+result2)))
            fileHandle.write('Re='+str(Re)+' r0/a='+str(r0)+' F/mu/U='+str(4*(result1+result2))+'\n')
            model.save()
    print('End of the simulation')
    fileHandle.close()
except KeyboardInterrupt:
    fileHandle.close()
