import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
w1=cq.Workplane('YZ',origin=(-2,0,0))
r=w0.sketch().arc((-34,24),(28,39),(-21,84)).arc((-92,70),(-34,24)).assemble().push([(-3,-74)]).circle(26).finalize().extrude(-16).union(w1.sketch().segment((-83,39),(-61,39)).arc((-48,0),(-9,-6)).arc((11,0),(29,13)).arc((78,71),(4,73)).arc((-28,75),(-52,52)).segment((-83,52)).close().assemble().finalize().extrude(-3))