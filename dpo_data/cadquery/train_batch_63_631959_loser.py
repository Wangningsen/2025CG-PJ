import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,30,0))
r=w0.workplane(offset=-82/2).moveTo(0,-2).box(200,58,82).union(w0.workplane(offset=21/2).moveTo(-17,2).cylinder(21,29))