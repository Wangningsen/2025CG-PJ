import cadquery as cq
w0=cq.Workplane('YZ',origin=(-5,0,0))
w1=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().segment((-100,-16),(-63,-62)).segment((37,19)).segment((100,19)).segment((100,37)).segment((14,37)).segment((-6,62)).close().assemble().push([(-34,0)]).circle(17,mode='s').finalize().extrude(11).union(w1.workplane(offset=-11/2).moveTo(-34,0).cylinder(11,17))