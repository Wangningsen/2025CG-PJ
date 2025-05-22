import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,46))
w1=cq.Workplane('YZ',origin=(28,0,0))
r=w0.workplane(offset=-92/2).moveTo(-53.5,-90.5).box(45,19,92).union(w0.workplane(offset=-59/2).moveTo(14,38).cylinder(59,62)).union(w1.sketch().arc((-24,13),(-20,10),(-15,13)).segment((-18,13)).arc((-19,11),(-21,13)).close().assemble().finalize().extrude(-41))