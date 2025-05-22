import cadquery as cq
w0=cq.Workplane('YZ',origin=(-67,0,0))
r=w0.sketch().arc((-3,-75),(96,-37),(41,56)).arc((-96,28),(-3,-75)).assemble().finalize().extrude(134)