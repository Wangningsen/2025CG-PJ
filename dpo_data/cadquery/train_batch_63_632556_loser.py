import cadquery as cq
w0=cq.Workplane('YZ',origin=(10,0,0))
w1=cq.Workplane('YZ',origin=(34,0,0))
r=w0.workplane(offset=-50/2).moveTo(-18,71).box(56,58,50).union(w0.sketch().segment((-59,12),(-55,8)).segment((-51,11)).arc((-55,13),(-57,16)).close().assemble().finalize().extrude(30)).union(w1.workplane(offset=-24/2).moveTo(27,-68).cylinder(24,32))