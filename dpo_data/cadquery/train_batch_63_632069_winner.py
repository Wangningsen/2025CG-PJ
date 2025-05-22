import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-83,0))
r=w0.sketch().arc((-63,70),(2,-100),(66,70)).arc((2,100),(-63,70)).assemble().finalize().extrude(166)