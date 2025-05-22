import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
r=w0.sketch().segment((-100,-37),(-29,-37)).arc((0,-46),(29,-37)).segment((100,-37)).segment((100,37)).segment((29,37)).arc((0,46),(-29,37)).segment((-100,37)).close().assemble().push([(-39,-16)]).circle(10,mode='s').finalize().extrude(-20).union(w0.workplane(offset=97/2).box(160,58,97))