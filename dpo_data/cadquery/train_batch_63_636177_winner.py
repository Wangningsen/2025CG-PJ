import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-61,-24),(-30,-58)).segment((61,24)).segment((30,58)).close().assemble().finalize().extrude(-200).union(w0.workplane(offset=-156/2).moveTo(15,25).cylinder(156,23))