import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.sketch().segment((-100,-37),(-27,-37)).arc((0,-46),(27,-37)).segment((100,-37)).segment((100,37)).segment((27,37)).arc((0,46),(-27,37)).segment((-100,37)).close().assemble().push([(-99,6)]).rect(2,4,mode='s').push([(-39,-15)]).circle(10,mode='s').finalize().extrude(-21).union(w0.workplane(offset=96/2).box(160,58,96))