import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-4,78),(-22,-75),(44,63)).arc((21,66),(-4,78)).assemble().finalize().extrude(-200)