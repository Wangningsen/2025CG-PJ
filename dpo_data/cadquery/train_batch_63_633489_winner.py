import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,56))
r=w0.workplane(offset=-113/2).moveTo(55.5,21).box(89,130,113).union(w0.workplane(offset=-30/2).moveTo(-82,-68).cylinder(30,18))