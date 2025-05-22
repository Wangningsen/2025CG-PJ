import cadquery as cq
w0=cq.Workplane('YZ',origin=(-1,0,0))
r=w0.sketch().arc((-37,6),(-100,-17),(-35,-31)).arc((100,4),(-37,6)).assemble().finalize().extrude(3)