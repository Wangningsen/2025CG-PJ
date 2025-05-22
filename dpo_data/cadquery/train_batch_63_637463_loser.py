import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().arc((20,98),(-40,-91),(58,81)).arc((36,88),(20,98)).assemble().finalize().extrude(-200)