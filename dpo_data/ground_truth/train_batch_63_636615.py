import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-9))
r=w0.workplane(offset=-37/2).cylinder(37,100).union(w0.workplane(offset=56/2).cylinder(56,29))