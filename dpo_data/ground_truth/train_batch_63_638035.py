import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-34,0))
r=w0.workplane(offset=-33/2).moveTo(-47,24).cylinder(33,53).union(w0.workplane(offset=101/2).moveTo(65,-42).cylinder(101,35))