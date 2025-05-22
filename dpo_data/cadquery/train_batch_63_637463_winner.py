import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((17,98),(-34,-94),(57,82)).arc((36,88),(17,98)).assemble().finalize().extrude(200)