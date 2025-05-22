import cadquery as cq
w0=cq.Workplane('YZ',origin=(-93,0,0))
r=w0.workplane(offset=67/2).moveTo(-89,-69).cylinder(67,11).union(w0.workplane(offset=186/2).moveTo(71,67.5).box(58,25,186))