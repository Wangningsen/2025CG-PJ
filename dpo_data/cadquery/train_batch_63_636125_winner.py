import cadquery as cq
w0=cq.Workplane('YZ',origin=(6,0,0))
w1=cq.Workplane('YZ',origin=(6,0,0))
r=w0.sketch().segment((-100,-16),(-63,-62)).segment((40,19)).segment((100,19)).segment((100,37)).segment((15,37)).segment((-6,62)).close().assemble().push([(-34,0)]).circle(17,mode='s').finalize().extrude(-11).union(w1.sketch().push([(-34,0)]).circle(17).circle(16,mode='s').finalize().extrude(-5))