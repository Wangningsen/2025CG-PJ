import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,19,0))
w1=cq.Workplane('YZ',origin=(-20,0,0))
r=w0.workplane(offset=-119/2).moveTo(-35,-48).cylinder(119,50).union(w0.workplane(offset=-85/2).moveTo(47,60).cylinder(85,38)).union(w0.sketch().push([(-35,-48)]).circle(2).reset().face(w0.sketch().segment((-37,-49),(-35,-49)).segment((-34,-49)).segment((-34,-47)).segment((-36,-47)).segment((-37,-47)).close().assemble(),mode='s').finalize().extrude(81)).union(w1.workplane(offset=-7/2).moveTo(42,-36).box(78,76,7))