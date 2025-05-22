import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
w1=cq.Workplane('YZ',origin=(37,0,0))
r=w0.workplane(offset=-76/2).cylinder(76,100).union(w1.sketch().arc((-48,31),(-46,33),(-48,35)).close().assemble().finalize().extrude(-50))