import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.workplane(offset=-69/2).moveTo(-60,81).cylinder(69,19).union(w0.sketch().segment((-43,-100),(56,-100)).segment((56,-62)).segment((79,-62)).segment((79,-26)).segment((56,-26)).segment((56,32)).segment((-43,32)).close().assemble().finalize().extrude(-5))