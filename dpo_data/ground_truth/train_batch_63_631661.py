import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,37,0))
r=w0.sketch().arc((-69,-93),(67,-19),(-31,100)).arc((-17,-3),(-69,-93)).assemble().finalize().extrude(-75)