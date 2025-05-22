import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-32))
w1=cq.Workplane('ZX',origin=(0,-32,0))
r=w0.sketch().segment((-83,-48),(-9,-48)).segment((-10,-41)).segment((81,-41)).segment((81,-2)).segment((-11,-2)).segment((-12,11)).segment((-83,11)).close().assemble().push([(56,-10.5)]).rect(32,3,mode='s').finalize().extrude(-41).union(w0.sketch().segment((2,-28),(27,-28)).arc((53,12),(100,6)).segment((100,46)).segment((63,46)).arc((51,48),(40,46)).segment((2,46)).close().assemble().finalize().extrude(44)).union(w1.workplane(offset=17/2).moveTo(58,-85).cylinder(17,15))