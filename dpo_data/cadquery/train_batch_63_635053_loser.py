import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,29,0))
r=w0.sketch().arc((1,-48),(-25,-83),(18,-83)).arc((94,-21),(1,-48)).assemble().push([(-10,-73)]).circle(3,mode='s').finalize().extrude(-58).union(w0.workplane(offset=-24/2).moveTo(-57,52).cylinder(24,43))