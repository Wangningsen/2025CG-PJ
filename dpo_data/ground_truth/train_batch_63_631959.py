import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,29,0))
r=w0.workplane(offset=-81/2).moveTo(0,-2).box(200,58,81).union(w0.workplane(offset=22/2).moveTo(-17,2).cylinder(22,29))