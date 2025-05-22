import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,93,0))
r=w0.sketch().segment((-42,66),(73,-89)).segment((100,-69)).segment((-16,85)).close().assemble().finalize().extrude(-186).union(w0.workplane(offset=-113/2).moveTo(-61,49).cylinder(113,39))