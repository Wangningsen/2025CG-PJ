import cadquery as cq
w0=cq.Workplane('YZ',origin=(20,0,0))
r=w0.workplane(offset=-104/2).moveTo(-96.5,-6).box(3,46,104).union(w0.workplane(offset=-67/2).moveTo(32.5,80.5).box(59,39,67)).union(w0.sketch().arc((82,-100),(98,-59),(82,-18)).close().assemble().finalize().extrude(64))