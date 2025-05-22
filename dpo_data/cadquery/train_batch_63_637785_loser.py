import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,40,0))
w1=cq.Workplane('ZX',origin=(0,32,0))
r=w0.sketch().push([(20,51)]).circle(49).rect(10,64,mode='s').finalize().extrude(-105).union(w0.workplane(offset=25/2).moveTo(-24,-58).cylinder(25,42)).union(w1.workplane(offset=33/2).moveTo(-24,-58).cylinder(33,34))