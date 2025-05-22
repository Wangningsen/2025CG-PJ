import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,19))
w1=cq.Workplane('ZX',origin=(0,-85,0))
r=w0.sketch().push([(-50,59)]).circle(26).reset().face(w0.sketch().segment((-18,13),(-15,13)).arc((-11,4),(1,11)).segment((10,11)).segment((10,-10)).arc((72,37),(1,76)).arc((1,65),(-11,68)).arc((-22,43),(-18,16)).close().assemble()).finalize().extrude(-103).union(w0.workplane(offset=-52/2).moveTo(-79,-61).cylinder(52,21)).union(w1.sketch().push([(45.5,43.5)]).rect(77,113).push([(45,44)]).circle(33,mode='s').finalize().extrude(15))