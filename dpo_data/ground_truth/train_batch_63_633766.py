import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-20,14),(-3,20)).arc((-12,19),(-20,14)).assemble().reset().face(w0.sketch().segment((0,20),(14,-20)).arc((19,4),(0,20)).assemble()).finalize().extrude(-200)