import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
w1=cq.Workplane('ZX',origin=(0,-31,0))
r=w0.workplane(offset=-49/2).moveTo(55,-50).cylinder(49,5).union(w0.sketch().segment((-100,81),(-76,52)).segment((-70,57)).segment((-94,86)).close().assemble().finalize().extrude(81)).union(w1.sketch().push([(55,-50.5)]).rect(90,71).push([(55,-51)]).circle(6,mode='s').finalize().extrude(5))