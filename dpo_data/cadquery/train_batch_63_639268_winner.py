import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-35,0))
r=w0.sketch().segment((-90,79),(-77,67)).segment((-56,67)).segment((-56,48)).segment((-57,48)).segment((-29,22)).segment((-29,30)).segment((-6,30)).segment((-6,49)).segment((-40,49)).segment((-57,93)).close().assemble().finalize().extrude(-65).union(w0.workplane(offset=135/2).moveTo(85,-88).cylinder(135,5))