import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,73,0))
r=w0.sketch().arc((-25,36),(-100,-1),(-24,-35)).arc((100,1),(-25,36)).assemble().finalize().extrude(-146)