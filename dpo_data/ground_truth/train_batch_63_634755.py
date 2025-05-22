import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.workplane(offset=-92/2).moveTo(-47,-57).cylinder(92,13).union(w0.sketch().arc((11,24),(57,29),(35,70)).segment((35,24)).segment((24,24)).segment((24,32)).segment((22,32)).segment((22,24)).close().assemble().finalize().extrude(108))