import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-17,0))
w1=cq.Workplane('XY',origin=(0,0,83))
r=w0.sketch().segment((-83,-19),(6,-19)).segment((6,26)).arc((43,35),(6,43)).segment((6,96)).segment((-83,96)).close().assemble().push([(24,35)]).rect(2,18,mode='s').finalize().extrude(117).union(w1.sketch().push([(-62.5,-45)]).rect(67,110).push([(-63,-42)]).circle(29,mode='s').finalize().extrude(-82))