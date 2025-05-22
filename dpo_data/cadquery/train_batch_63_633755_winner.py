import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
r=w0.sketch().arc((-100,56),(-16,-31),(100,-55)).arc((-9,-15),(-100,56)).assemble().finalize().extrude(22)