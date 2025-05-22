import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,44,0))
r=w0.sketch().arc((22,-100),(-24,14),(85,71)).arc((-79,35),(22,-100)).assemble().finalize().extrude(-87)