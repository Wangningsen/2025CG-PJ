import cadquery as cq
w0=cq.Workplane('YZ',origin=(-45,0,0))
w1=cq.Workplane('YZ',origin=(-44,0,0))
r=w0.sketch().segment((-56,9),(-55,9)).arc((-44,-98),(22,-9)).segment((86,-9)).segment((86,50)).segment((-1,50)).segment((-1,13)).arc((-13,17),(-26,17)).segment((-33,17)).segment((-33,100)).segment((-56,100)).segment((-56,17)).segment((-56,11)).close().assemble().finalize().extrude(45).union(w0.workplane(offset=90/2).moveTo(-54,54).cylinder(90,7)).union(w1.workplane(offset=14/2).moveTo(-54,54).cylinder(14,7))