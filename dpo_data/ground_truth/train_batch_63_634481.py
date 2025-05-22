import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.sketch().arc((-11,86),(-5,-30),(63,65)).arc((32,98),(-11,86)).assemble().finalize().extrude(13).union(w0.workplane(offset=15/2).moveTo(-6,-31).cylinder(15,69))