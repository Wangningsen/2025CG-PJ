import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,11,0))
r=w0.sketch().arc((-47,-20),(-62,-88),(6,-72)).arc((5,-70),(7,-69)).arc((7,-52),(1,-36)).arc((74,48),(-10,-25)).arc((-27,-18),(-45,-19)).arc((-45,-23),(-47,-20)).assemble().push([(-36,-37)]).circle(4,mode='s').finalize().extrude(-76).union(w0.workplane(offset=55/2).moveTo(-78,43).box(24,114,55))