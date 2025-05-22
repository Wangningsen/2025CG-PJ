import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,43,0))
r=w0.sketch().arc((22,-100),(-22,19),(85,71)).arc((-80,32),(22,-100)).assemble().finalize().extrude(-86)