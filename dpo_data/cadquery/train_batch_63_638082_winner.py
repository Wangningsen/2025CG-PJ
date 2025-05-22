import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-73,0))
r=w0.sketch().arc((-24,-35),(100,-1),(-24,37)).arc((-100,0),(-24,-35)).assemble().finalize().extrude(146)