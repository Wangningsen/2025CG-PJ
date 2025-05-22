import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-71))
w1=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.workplane(offset=171/2).moveTo(0,34).box(156,16,171).union(w1.sketch().segment((-29,-100),(-10,-100)).segment((-10,-56)).arc((3,-34),(-10,-12)).segment((-10,31)).segment((-29,31)).segment((-29,-12)).arc((-42,-34),(-29,-56)).close().assemble().finalize().extrude(62))