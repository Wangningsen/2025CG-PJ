import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,42,0))
r=w0.sketch().segment((22,-9),(22,22)).arc((38,-54),(100,-9)).close().assemble().finalize().extrude(-139).union(w0.workplane(offset=55/2).moveTo(-38.5,12).box(123,90,55))