import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,64,0))
w1=cq.Workplane('YZ',origin=(85,0,0))
r=w0.sketch().segment((19,-94),(39,-100)).segment((78,17)).segment((58,24)).close().assemble().finalize().extrude(-128).union(w0.workplane(offset=-46/2).moveTo(-31.5,-56.5).box(93,33,46)).union(w0.workplane(offset=-14/2).moveTo(38,61).cylinder(14,39)).union(w1.sketch().segment((21,-11),(45,-11)).segment((45,11)).segment((40,11)).segment((40,12)).segment((45,12)).segment((45,29)).segment((21,29)).close().assemble().finalize().extrude(-54))