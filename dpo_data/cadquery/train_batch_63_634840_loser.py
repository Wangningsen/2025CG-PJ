import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
r=w0.workplane(offset=-89/2).moveTo(23,76).cylinder(89,19).union(w0.workplane(offset=-86/2).moveTo(-67.5,-60.5).box(65,69,86)).union(w0.workplane(offset=19/2).moveTo(96,42).cylinder(19,4))