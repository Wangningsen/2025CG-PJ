import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,2))
w1=cq.Workplane('XY',origin=(0,0,76))
r=w0.workplane(offset=-95/2).moveTo(-47,-63).cylinder(95,37).union(w1.sketch().arc((-5,57),(45,-23),(60,69)).arc((24,100),(-5,57)).assemble().push([(11,18.5)]).rect(26,27,mode='s').finalize().extrude(17))