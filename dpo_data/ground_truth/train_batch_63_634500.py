import cadquery as cq
w0=cq.Workplane('YZ',origin=(1,0,0))
r=w0.sketch().arc((-39,7),(-100,-21),(-33,-29)).arc((99,11),(-39,7)).assemble().finalize().extrude(-3)