import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,24,0))
w1=cq.Workplane('ZX',origin=(0,55,0))
r=w0.sketch().segment((-100,-20),(-98,-20)).segment((-96,-14)).segment((-100,-14)).close().assemble().finalize().extrude(-80).union(w1.sketch().push([(61,0)]).circle(39).rect(14,62,mode='s').finalize().extrude(-101))