import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,80,0))
r=w0.sketch().arc((-47,-88),(-43,-85),(-43,-90)).arc((10,99),(-47,-88)).assemble().finalize().extrude(-159)