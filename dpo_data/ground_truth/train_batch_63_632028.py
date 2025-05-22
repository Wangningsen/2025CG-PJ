import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,7))
w1=cq.Workplane('YZ',origin=(1,0,0))
r=w0.sketch().segment((-19,61),(-15,54)).arc((-11,57),(-7,59)).segment((-12,66)).close().assemble().finalize().extrude(93).union(w1.workplane(offset=18/2).moveTo(-34,-67).cylinder(18,33))