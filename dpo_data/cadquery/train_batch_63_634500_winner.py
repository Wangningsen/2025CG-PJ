import cadquery as cq
w0=cq.Workplane('YZ',origin=(-1,0,0))
r=w0.sketch().arc((-41,10),(-100,-16),(-36,-28)).arc((99,13),(-41,10)).assemble().finalize().extrude(3)