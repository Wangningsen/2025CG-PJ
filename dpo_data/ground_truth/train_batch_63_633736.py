import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,18))
w1=cq.Workplane('ZX',origin=(0,-70,0))
r=w0.sketch().push([(-50,59)]).circle(26).reset().face(w0.sketch().segment((-12,5),(-12,11)).segment((10,11)).segment((10,-10)).arc((50,75),(-12,5)).assemble()).finalize().extrude(-102).union(w0.workplane(offset=-51/2).moveTo(-80,-61).cylinder(51,20)).union(w1.sketch().push([(45,43.5)]).rect(76,113).push([(45,44)]).circle(33,mode='s').finalize().extrude(-15))