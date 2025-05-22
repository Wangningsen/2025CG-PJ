import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
r=w0.workplane(offset=-94/2).cylinder(94,3).union(w0.workplane(offset=68/2).cylinder(68,27)).union(w0.workplane(offset=106/2).box(38,18,106))