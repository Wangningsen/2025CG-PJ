import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,22,0))
r=w0.workplane(offset=-107/2).moveTo(-47,10).cylinder(107,53).union(w0.sketch().segment((41,2),(47,-63)).segment((100,-58)).segment((94,6)).close().assemble().finalize().extrude(63))