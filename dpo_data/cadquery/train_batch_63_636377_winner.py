import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,13,0))
w1=cq.Workplane('XY',origin=(0,0,7))
r=w0.workplane(offset=-91/2).moveTo(-18.5,-39).box(59,34,91).union(w0.sketch().push([(6,-63)]).rect(84,74).push([(27,-72)]).circle(4,mode='s').finalize().extrude(-73)).union(w1.sketch().segment((47,71),(100,71)).segment((100,78)).segment((77,78)).arc((76,77),(74,78)).segment((47,78)).close().assemble().finalize().extrude(-38))