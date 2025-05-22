import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,13,0))
w1=cq.Workplane('XY',origin=(0,0,-31))
r=w0.workplane(offset=-91/2).moveTo(-18.5,-39).box(59,34,91).union(w0.sketch().push([(6,-63)]).rect(84,74).push([(26,-72)]).circle(4,mode='s').finalize().extrude(-73)).union(w1.workplane(offset=38/2).moveTo(73.5,74.5).box(53,7,38))