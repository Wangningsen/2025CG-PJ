import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
w1=cq.Workplane('YZ',origin=(-10,0,0))
r=w0.sketch().segment((-16,-55),(-6,-43)).segment((7,-54)).arc((-10,55),(-16,-55)).assemble().finalize().extrude(-97).union(w0.workplane(offset=69/2).moveTo(-7,0).cylinder(69,10)).union(w1.sketch().segment((-6,-100),(-1,-100)).arc((-4,-99),(-6,-99)).close().assemble().finalize().extrude(72))