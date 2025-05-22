import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-15,0))
r=w0.workplane(offset=6/2).moveTo(-56,0).cylinder(6,44).union(w0.workplane(offset=29/2).moveTo(86,-25).cylinder(29,14))