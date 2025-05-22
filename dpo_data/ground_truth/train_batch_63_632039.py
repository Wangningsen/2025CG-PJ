import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,12,0))
r=w0.sketch().push([(4,72)]).circle(28).push([(-11,70)]).circle(12,mode='s').reset().face(w0.sketch().segment((0,-77),(10,-100)).segment((15,-100)).segment((15,-80)).arc((58,-51),(14,-77)).close().assemble()).finalize().extrude(-38).union(w0.workplane(offset=13/2).moveTo(-32,4).cylinder(13,34))