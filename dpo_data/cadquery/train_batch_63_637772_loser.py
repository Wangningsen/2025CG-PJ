import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,23,0))
r=w0.sketch().segment((-98,-20),(-45,-95)).segment((63,-19)).segment((10,54)).close().assemble().push([(-18,-20)]).circle(18,mode='s').finalize().extrude(-66).union(w0.sketch().segment((-100,-85),(65,-85)).segment((65,-56)).arc((70,75),(-59,51)).segment((-100,51)).close().assemble().finalize().extrude(20))