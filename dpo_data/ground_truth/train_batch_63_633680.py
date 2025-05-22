import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
r=w0.sketch().arc((-25,-7),(54,-91),(17,17)).arc((-56,92),(-25,-7)).assemble().push([(-29,46)]).circle(16,mode='s').finalize().extrude(-15)