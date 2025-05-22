import cadquery as cq
w0=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.sketch().segment((-8,10),(-8,50)).arc((-36,-9),(17,-47)).arc((65,-37),(74,10)).close().assemble().finalize().extrude(-71).union(w0.workplane(offset=129/2).moveTo(-75,17).cylinder(129,2))