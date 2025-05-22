import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,91,0))
r=w0.sketch().arc((73,-69),(71,-46),(90,-44)).arc((-82,58),(73,-69)).assemble().circle(31,mode='s').finalize().extrude(-182)