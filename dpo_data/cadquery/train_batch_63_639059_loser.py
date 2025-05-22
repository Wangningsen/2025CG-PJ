import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,65,0))
r=w0.workplane(offset=-147/2).moveTo(34,0).cylinder(147,66).union(w0.sketch().segment((-100,-1),(-39,-8)).arc((-28,-26),(-14,-11)).segment((-11,-11)).segment((-12,-9)).segment((-14,-9)).arc((-25,0),(-38,-8)).segment((-99,1)).close().assemble().finalize().extrude(17))