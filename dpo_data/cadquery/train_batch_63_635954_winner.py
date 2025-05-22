import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-28,-63),(-5,-62),(15,-67)).arc((4,67),(-28,-63)).assemble().finalize().extrude(-200)