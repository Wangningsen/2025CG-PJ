import cadquery as cq
w0=cq.Workplane('YZ',origin=(-36,0,0))
r=w0.sketch().arc((-16,-100),(0,-97),(16,-100)).segment((16,100)).segment((-16,100)).close().assemble().finalize().extrude(72)