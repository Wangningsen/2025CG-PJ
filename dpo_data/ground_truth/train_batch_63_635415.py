import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,2))
w1=cq.Workplane('XY',origin=(0,0,76))
r=w0.workplane(offset=-95/2).moveTo(-47,-63).cylinder(95,37).union(w1.sketch().arc((-6,56),(43,-23),(60,68)).arc((20,99),(-6,56)).assemble().push([(11,18)]).rect(26,26,mode='s').finalize().extrude(17))