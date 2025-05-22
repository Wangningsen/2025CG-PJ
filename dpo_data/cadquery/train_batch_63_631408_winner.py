import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,80,0))
r=w0.sketch().segment((-47,-88),(-41,-88)).segment((-41,-91)).arc((38,93),(-47,-88)).assemble().finalize().extrude(-160)