import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-20,0))
r=w0.sketch().push([(-36,75.5)]).rect(52,49).push([(-29,59)]).circle(3,mode='s').finalize().extrude(11).union(w0.sketch().push([(-48,-97)]).circle(3).reset().face(w0.sketch().segment((25,-6),(40,-14)).segment((62,30)).segment((46,38)).close().assemble()).finalize().extrude(39))