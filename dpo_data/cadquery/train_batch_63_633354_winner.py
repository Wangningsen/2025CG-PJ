import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,4,0))
w1=cq.Workplane('ZX',origin=(0,-23,0))
r=w0.sketch().arc((1,29),(1,-75),(92,-29)).segment((70,-29)).segment((70,33)).arc((40,42),(11,32)).arc((5,31),(1,29)).assemble().finalize().extrude(-45).union(w0.sketch().segment((-100,37),(-49,-35)).segment((-37,-26)).segment((-88,45)).close().assemble().finalize().extrude(38)).union(w1.workplane(offset=27/2).moveTo(41,24).cylinder(27,59))