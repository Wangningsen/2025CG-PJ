import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,19))
r=w0.workplane(offset=-119/2).moveTo(73,-73).cylinder(119,8).union(w0.sketch().segment((-54,32),(-53,70)).arc((0,-43),(-16,81)).segment((-16,72)).segment((-10,72)).segment((-9,11)).segment((-24,12)).segment((-25,23)).arc((-39,24),(-53,32)).close().assemble().finalize().extrude(81))