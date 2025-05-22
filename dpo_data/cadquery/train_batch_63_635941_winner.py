import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,25))
w1=cq.Workplane('XY',origin=(0,0,28))
r=w0.workplane(offset=31/2).moveTo(30.5,-61.5).box(109,31,31).union(w0.sketch().segment((-100,-13),(-87,-49)).segment((-74,-44)).arc((-25,-56),(6,-14)).segment((89,-23)).segment((100,63)).segment((-8,77)).segment((-14,28)).segment((-16,31)).segment((-28,34)).arc((-71,26),(-89,-10)).close().assemble().finalize().extrude(45)).union(w1.workplane(offset=-99/2).moveTo(-14,46).cylinder(99,3))