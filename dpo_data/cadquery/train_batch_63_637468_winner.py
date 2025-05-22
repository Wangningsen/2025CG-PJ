import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,45,0))
r=w0.sketch().segment((-55,-14),(25,-14)).segment((25,-9)).segment((-54,-9)).arc((-54,-11),(-55,-14)).assemble().finalize().extrude(-145).union(w0.workplane(offset=55/2).moveTo(7,0).cylinder(55,48))