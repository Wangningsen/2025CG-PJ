import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-21))
w1=cq.Workplane('ZX',origin=(0,22,0))
r=w0.workplane(offset=-79/2).moveTo(47,0).cylinder(79,46).union(w1.sketch().arc((0,-56),(93,-67),(37,8)).arc((-34,5),(0,-56)).assemble().finalize().extrude(-43))