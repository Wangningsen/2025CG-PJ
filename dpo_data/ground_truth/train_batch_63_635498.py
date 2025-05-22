import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-33,0))
r=w0.workplane(offset=22/2).moveTo(0,-28.5).box(102,143,22).union(w0.sketch().segment((-52,-38),(52,-38)).arc((0,25),(-52,-38)).assemble().push([(0,-28)]).circle(4,mode='s').finalize().extrude(50)).union(w0.sketch().segment((-11,4),(11,-1)).segment((11,100)).segment((-11,100)).close().assemble().finalize().extrude(66))