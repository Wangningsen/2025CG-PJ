import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-30,0))
r=w0.workplane(offset=-70/2).moveTo(2,14).box(42,16,70).union(w0.workplane(offset=130/2).moveTo(-11.5,-20.5).box(23,3,130))