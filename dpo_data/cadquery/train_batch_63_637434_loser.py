import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,45,0))
r=w0.workplane(offset=-89/2).moveTo(-90,9).cylinder(89,5).union(w0.workplane(offset=-8/2).moveTo(76,0).box(38,200,8))