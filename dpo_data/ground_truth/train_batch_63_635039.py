import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-56,0))
r=w0.sketch().segment((-97,-7),(-22,-100)).segment((-8,-89)).segment((-8,-86)).segment((-4,-86)).segment((87,-12)).segment((75,3)).arc((75,89),(-8,64)).close().assemble().finalize().extrude(111)