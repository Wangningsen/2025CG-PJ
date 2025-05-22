import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-20,14),(-4,20)).arc((-13,19),(-20,14)).assemble().reset().face(w0.sketch().segment((0,20),(14,-20)).arc((18,6),(0,20)).assemble()).finalize().extrude(200)