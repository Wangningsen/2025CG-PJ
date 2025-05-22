import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().arc((-3,78),(-24,-74),(51,59)).arc((23,65),(-3,78)).assemble().finalize().extrude(200)