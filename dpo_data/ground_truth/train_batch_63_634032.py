import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-43,0))
r=w0.sketch().segment((-16,-67),(100,-67)).segment((100,-15)).segment((6,-15)).segment((6,-7)).segment((-16,-7)).close().assemble().reset().face(w0.sketch().segment((-6,-34),(0,-39)).segment((9,-29)).segment((2,-24)).close().assemble(),mode='s').finalize().extrude(50).union(w0.workplane(offset=87/2).moveTo(-54,21).cylinder(87,46))