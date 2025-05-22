import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-29,-62),(-7,-62),(15,-67)).arc((8,67),(-29,-62)).assemble().finalize().extrude(-200)