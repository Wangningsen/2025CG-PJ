import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,9))
r=w0.sketch().segment((-100,32),(-87,-33)).segment((-31,-21)).segment((-31,-72)).segment((100,-72)).segment((100,13)).segment((17,13)).segment((8,55)).close().assemble().finalize().extrude(-49).union(w0.sketch().arc((-41,52),(-36,61),(-41,72)).close().assemble().push([(84.5,61)]).rect(7,22).finalize().extrude(31))