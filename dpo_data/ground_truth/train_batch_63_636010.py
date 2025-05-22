import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-43))
r=w0.workplane(offset=5/2).moveTo(71,-31).cylinder(5,29).union(w0.workplane(offset=85/2).moveTo(-79,55.5).box(42,9,85))