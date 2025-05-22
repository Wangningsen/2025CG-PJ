import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-2,6),(2,-6)).arc((1,0),(-2,6)).assemble().finalize().extrude(200)