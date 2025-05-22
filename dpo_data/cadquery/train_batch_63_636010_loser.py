import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-43))
r=w0.workplane(offset=6/2).moveTo(71,-31).cylinder(6,29).union(w0.workplane(offset=86/2).moveTo(-79,55.5).box(42,9,86))