import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
w1=cq.Workplane('XY',origin=(0,0,0))
r=w0.workplane(offset=-70/2).moveTo(68,60.5).box(6,79,70).union(w0.sketch().segment((42,-88),(44,-88)).arc((48,-81),(56,-75)).segment((42,-65)).close().assemble().finalize().extrude(-2)).union(w0.workplane(offset=56/2).moveTo(3,-78).cylinder(56,22)).union(w1.sketch().push([(-77.5,14)]).rect(45,36).push([(-78,13)]).circle(6,mode='s').finalize().extrude(-71))