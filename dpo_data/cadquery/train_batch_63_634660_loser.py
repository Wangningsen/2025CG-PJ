import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,19,0))
r=w0.workplane(offset=-119/2).moveTo(-35,-48).cylinder(119,50).union(w0.workplane(offset=-85/2).moveTo(47,60).cylinder(85,38)).union(w0.sketch().segment((-74,-27),(-34,-27)).segment((-36,-50)).segment((-35,-50)).segment((-33,-27)).segment((2,-27)).segment((2,-20)).segment((-74,-20)).close().assemble().finalize().extrude(62))