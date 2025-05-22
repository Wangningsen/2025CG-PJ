import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,15,0))
w1=cq.Workplane('XY',origin=(0,0,11))
r=w0.sketch().arc((-95,-22),(-52,-3),(-69,-46)).arc((-18,38),(-95,-22)).assemble().finalize().extrude(-31).union(w1.workplane(offset=89/2).moveTo(15,0).cylinder(89,33))