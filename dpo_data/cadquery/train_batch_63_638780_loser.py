import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,25,0))
r=w0.sketch().segment((-41,-11),(2,-78)).segment((100,-11)).segment((40,78)).segment((-41,24)).close().assemble().finalize().extrude(-90).union(w0.workplane(offset=-88/2).moveTo(-43.5,16.5).box(113,55,88)).union(w0.workplane(offset=40/2).moveTo(22,-23).cylinder(40,44))