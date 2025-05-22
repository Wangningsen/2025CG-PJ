import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-27))
r=w0.workplane(offset=-4/2).moveTo(0,7).box(86,102,4).union(w0.sketch().segment((-99,-86),(-45,-86)).arc((2,-100),(49,-86)).segment((99,-86)).segment((99,100)).segment((-99,100)).close().assemble().push([(2,-12)]).circle(54,mode='s').finalize().extrude(58))