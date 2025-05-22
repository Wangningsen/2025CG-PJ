import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().arc((-10,-25),(-65,-85),(0,-35)).arc((76,46),(-10,-25)).assemble().push([(-36,-37)]).circle(4,mode='s').finalize().extrude(-76).union(w0.workplane(offset=55/2).moveTo(-78,43).box(24,114,55))