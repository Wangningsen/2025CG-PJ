import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,65,0))
r=w0.workplane(offset=-147/2).moveTo(34,0).cylinder(147,66).union(w0.sketch().segment((-100,-3),(-35,-10)).segment((-33,-22)).segment((-12,-34)).arc((-54,-1),(-100,-3)).assemble().finalize().extrude(17))