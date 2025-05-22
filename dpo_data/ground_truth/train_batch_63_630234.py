import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-30,0))
r=w0.sketch().push([(16,33)]).circle(67).circle(21,mode='s').finalize().extrude(52).union(w0.sketch().segment((-83,-100),(21,-100)).segment((21,-11)).arc((37,73),(-24,14)).segment((-83,14)).close().assemble().finalize().extrude(60))