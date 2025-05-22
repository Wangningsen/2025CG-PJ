import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
r=w0.workplane(offset=-115/2).moveTo(0,-16).box(104,86,115).union(w0.workplane(offset=-10/2).moveTo(22,56).cylinder(10,3)).union(w0.workplane(offset=85/2).moveTo(0,-15).cylinder(85,10))