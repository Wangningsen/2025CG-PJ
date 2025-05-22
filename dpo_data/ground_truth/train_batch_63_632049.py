import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,55))
w1=cq.Workplane('ZX',origin=(0,100,0))
r=w0.workplane(offset=-110/2).moveTo(36,69).cylinder(110,4).union(w1.sketch().arc((9,-39),(30,-37),(52,-40)).arc((37,-11),(9,3)).close().assemble().finalize().extrude(-200))