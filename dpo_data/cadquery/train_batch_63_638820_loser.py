import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-26))
w1=cq.Workplane('ZX',origin=(0,-71,0))
r=w0.sketch().push([(-49,8)]).circle(51).push([(56,21)]).rect(86,90).finalize().extrude(46).union(w0.workplane(offset=52/2).moveTo(56,21).box(88,98,52)).union(w1.sketch().arc((-21,33),(-11,54),(-21,76)).close().assemble().finalize().extrude(38))