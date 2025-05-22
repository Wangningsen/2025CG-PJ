import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-34,0))
r=w0.workplane(offset=-30/2).moveTo(11,53).cylinder(30,47).union(w0.workplane(offset=98/2).moveTo(-48,-90).cylinder(98,10))