import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-7,0))
r=w0.sketch().arc((-27,-9),(52,-93),(15,17)).arc((-55,93),(-27,-9)).assemble().push([(-29,47)]).circle(16,mode='s').finalize().extrude(15)