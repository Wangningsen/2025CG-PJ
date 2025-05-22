import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.workplane(offset=40/2).cylinder(40,85).union(w0.sketch().arc((-16,2),(16,0),(-16,3)).arc((-12,2),(-16,2)).assemble().push([(0,-1)]).circle(7,mode='s').finalize().extrude(200))