import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
w1=cq.Workplane('XY',origin=(0,0,40))
r=w0.sketch().push([(23.5,-76.5)]).rect(27,47).push([(23.5,-77)]).rect(19,8,mode='s').finalize().extrude(-50).union(w0.workplane(offset=34/2).moveTo(-36,3).cylinder(34,4)).union(w1.workplane(offset=-80/2).moveTo(40,28).cylinder(80,60))