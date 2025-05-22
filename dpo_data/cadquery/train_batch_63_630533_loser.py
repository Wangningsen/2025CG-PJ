import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().push([(31.5,-12)]).rect(65,126).push([(31,-12)]).circle(13,mode='s').finalize().extrude(15).union(w0.sketch().arc((-64,34),(-22,38),(21,22)).segment((23,22)).segment((23,21)).arc((28,18),(32,14)).segment((34,18)).segment((-14,75)).close().assemble().finalize().extrude(200))