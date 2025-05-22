import cadquery as cq
w0=cq.Workplane('YZ',origin=(44,0,0))
r=w0.sketch().segment((-61,-91),(26,-100)).arc((24,-16),(61,83)).segment((52,85)).arc((46,86),(41,87)).segment((-35,100)).close().assemble().finalize().extrude(-88)