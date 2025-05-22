import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,13,0))
r=w0.sketch().push([(4,72)]).circle(28).push([(-11,70)]).circle(12,mode='s').reset().face(w0.sketch().segment((0,-77),(10,-100)).segment((15,-98)).segment((15,-79)).arc((64,-60),(13,-71)).close().assemble()).finalize().extrude(-38).union(w0.workplane(offset=12/2).moveTo(-32,4).cylinder(12,34))