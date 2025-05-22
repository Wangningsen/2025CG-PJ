import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
r=w0.workplane(offset=-22/2).moveTo(0,33.5).box(114,133,22).union(w0.workplane(offset=12/2).moveTo(-3,-75).cylinder(12,25))