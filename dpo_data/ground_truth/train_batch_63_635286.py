import cadquery as cq
w0=cq.Workplane('YZ',origin=(-43,0,0))
r=w0.sketch().segment((-61,-91),(26,-100)).arc((26,-4),(61,83)).segment((-35,100)).close().assemble().finalize().extrude(87)