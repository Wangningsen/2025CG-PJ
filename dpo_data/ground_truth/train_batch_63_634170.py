import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-57,0))
w1=cq.Workplane('XY',origin=(0,0,-34))
r=w0.workplane(offset=-43/2).cylinder(43,91).union(w0.workplane(offset=157/2).moveTo(-64,22.5).box(26,63,157)).union(w1.sketch().push([(23,-11)]).circle(23).push([(7.5,-13)]).rect(9,14,mode='s').push([(24.5,-20.5)]).rect(19,7,mode='s').finalize().extrude(-35))