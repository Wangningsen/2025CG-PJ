import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
w1=cq.Workplane('XY',origin=(0,0,-55))
r=w0.sketch().arc((9,-39),(30,-37),(52,-40)).arc((35,-9),(9,3)).close().assemble().finalize().extrude(-200).union(w1.sketch().push([(36,69)]).circle(4).circle(2,mode='s').finalize().extrude(110))