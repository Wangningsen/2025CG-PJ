import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-24))
r=w0.sketch().segment((68,14),(69,11)).segment((100,19)).segment((99,22)).close().assemble().finalize().extrude(-40).union(w0.sketch().segment((-100,-22),(-73,-22)).arc((-78,-4),(-74,14)).segment((-100,14)).close().assemble().finalize().extrude(89))