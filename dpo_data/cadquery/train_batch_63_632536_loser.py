import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-11))
r=w0.workplane(offset=-89/2).moveTo(5,0).cylinder(89,14).union(w0.sketch().segment((-31,-12),(-4,-12)).segment((-4,-38)).segment((15,-38)).segment((15,-12)).segment((31,-12)).segment((31,7)).segment((15,7)).segment((15,38)).segment((-4,38)).segment((-4,7)).segment((-31,7)).close().assemble().finalize().extrude(111))