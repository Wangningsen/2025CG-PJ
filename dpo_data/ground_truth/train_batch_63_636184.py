import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,36,0))
r=w0.workplane(offset=-100/2).moveTo(18,-1).box(80,114,100).union(w0.workplane(offset=-100/2).moveTo(45,-8).cylinder(100,55)).union(w0.workplane(offset=27/2).moveTo(-93,56).cylinder(27,7))