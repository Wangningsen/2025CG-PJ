import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
w1=cq.Workplane('XY',origin=(0,0,40))
r=w0.sketch().push([(23.5,-76.5)]).rect(27,47).push([(23.5,-77)]).rect(19,8,mode='s').finalize().extrude(-50).union(w0.sketch().segment((-39,-6),(-33,-6)).arc((-34,2),(-33,10)).segment((-39,10)).close().assemble().finalize().extrude(78)).union(w1.workplane(offset=-80/2).moveTo(40,28).cylinder(80,60))