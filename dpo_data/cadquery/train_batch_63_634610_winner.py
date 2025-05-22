import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-44,0))
r=w0.sketch().arc((22,-100),(-20,23),(85,71)).arc((-78,37),(22,-100)).assemble().finalize().extrude(87)