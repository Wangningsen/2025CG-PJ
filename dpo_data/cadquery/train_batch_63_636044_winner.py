import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-43,0))
w1=cq.Workplane('XY',origin=(0,0,16))
r=w0.sketch().segment((-71,-14),(13,-14)).arc((45,-62),(15,-13)).segment((15,100)).segment((-71,100)).close().assemble().finalize().extrude(86).union(w1.workplane(offset=55/2).moveTo(-83.5,15).box(33,14,55))