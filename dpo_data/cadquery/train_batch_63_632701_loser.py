import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-74))
r=w0.workplane(offset=-26/2).moveTo(0,0).cylinder(26,52).union(w0.workplane(offset=174/2).box(118,106,174))