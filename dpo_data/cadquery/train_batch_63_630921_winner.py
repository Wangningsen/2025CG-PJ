import cadquery as cq
w0=cq.Workplane('YZ',origin=(80,0,0))
r=w0.workplane(offset=-160/2).moveTo(18,0).cylinder(160,82).union(w0.sketch().segment((-31,-68),(31,-68)).segment((31,-40)).arc((0,-52),(-31,-40)).close().assemble().finalize().extrude(-130)).union(w0.workplane(offset=-140/2).moveTo(-34,12).cylinder(140,66))