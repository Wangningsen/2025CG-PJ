import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-33,0))
r=w0.workplane(offset=22/2).moveTo(0,-28.5).box(102,143,22).union(w0.sketch().segment((-53,-38),(53,-38)).arc((0,25),(-53,-38)).assemble().push([(0,-30)]).circle(4,mode='s').finalize().extrude(50)).union(w0.workplane(offset=66/2).moveTo(0,50.5).box(22,99,66))