import cadquery as cq
w0=cq.Workplane('YZ',origin=(-59,0,0))
r=w0.workplane(offset=8/2).moveTo(-91,-17).cylinder(8,9).union(w0.workplane(offset=118/2).moveTo(42.5,0).box(115,100,118))