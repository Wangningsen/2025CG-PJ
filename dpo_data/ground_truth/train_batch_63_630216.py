import cadquery as cq
w0=cq.Workplane('YZ',origin=(-72,0,0))
r=w0.workplane(offset=35/2).moveTo(-29,-68).cylinder(35,32).union(w0.sketch().arc((35,98),(50,66),(37,99)).arc((36,98),(35,98)).assemble().finalize().extrude(144))