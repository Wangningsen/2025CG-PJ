import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,42,0))
r=w0.sketch().segment((22,-9),(22,22)).arc((37,-54),(100,-9)).close().assemble().reset().face(w0.sketch().segment((9,-5),(13,-7)).segment((14,-5)).segment((10,-3)).close().assemble(),mode='s').finalize().extrude(-139).union(w0.workplane(offset=55/2).moveTo(-38.5,12).box(123,90,55))