import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,7))
r=w0.workplane(offset=-107/2).box(76,100,107).union(w0.workplane(offset=93/2).cylinder(93,37))