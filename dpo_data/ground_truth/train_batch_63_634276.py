import cadquery as cq
w0=cq.Workplane('YZ',origin=(57,0,0))
r=w0.sketch().arc((-9,-5),(10,1),(-9,4)).arc((-11,-1),(-9,-5)).assemble().finalize().extrude(-157).union(w0.workplane(offset=43/2).box(42,86,43))