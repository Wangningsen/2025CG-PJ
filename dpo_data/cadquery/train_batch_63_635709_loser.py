import cadquery as cq
w0=cq.Workplane('YZ',origin=(-26,0,0))
w1=cq.Workplane('YZ',origin=(-44,0,0))
r=w0.workplane(offset=69/2).moveTo(39,-45).cylinder(69,55).union(w1.sketch().arc((-71,-7),(-50,3),(-26,1)).arc((-45,100),(-71,-1)).close().assemble().finalize().extrude(17))