import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,80,0))
r=w0.sketch().segment((-50,-87),(-41,-87)).segment((-41,-91)).arc((40,92),(-50,-87)).assemble().finalize().extrude(-160)