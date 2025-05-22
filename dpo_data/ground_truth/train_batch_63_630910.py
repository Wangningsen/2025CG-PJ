import cadquery as cq
w0=cq.Workplane('YZ',origin=(-59,0,0))
r=w0.workplane(offset=9/2).moveTo(-91,-16).cylinder(9,9).union(w0.workplane(offset=118/2).moveTo(42.5,0).box(115,100,118))