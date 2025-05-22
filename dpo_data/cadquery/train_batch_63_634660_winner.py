import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,19,0))
w1=cq.Workplane('YZ',origin=(-27,0,0))
r=w0.workplane(offset=-119/2).moveTo(-35,-48).cylinder(119,50).union(w0.workplane(offset=-85/2).moveTo(47,60).cylinder(85,38)).union(w0.sketch().segment((-36,-49),(-34,-49)).segment((-34,-46)).arc((-35,-47),(-36,-49)).assemble().finalize().extrude(81)).union(w1.workplane(offset=7/2).moveTo(40.5,-36.5).box(81,75,7))