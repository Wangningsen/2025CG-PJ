import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,11))
w1=cq.Workplane('ZX',origin=(0,15,0))
r=w0.workplane(offset=89/2).moveTo(15,0).cylinder(89,33).union(w1.sketch().arc((-95,-22),(-52,-2),(-69,-46)).arc((-21,-40),(-1,4)).arc((13,18),(-6,23)).arc((-73,44),(-95,-22)).assemble().finalize().extrude(-31))