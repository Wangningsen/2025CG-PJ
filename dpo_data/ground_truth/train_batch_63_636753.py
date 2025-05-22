import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-18,0))
r=w0.workplane(offset=-54/2).moveTo(41,-47).cylinder(54,53).union(w0.workplane(offset=90/2).moveTo(-51.5,48).box(85,104,90))