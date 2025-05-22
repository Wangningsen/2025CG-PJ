import cadquery as cq
w0=cq.Workplane('YZ',origin=(-2,0,0))
r=w0.sketch().arc((-7,-4),(0,-100),(7,-4)).arc((0,100),(-7,-4)).assemble().finalize().extrude(4)