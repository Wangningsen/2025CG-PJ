import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-2,78),(-20,-75),(50,60)).arc((23,65),(-2,78)).assemble().finalize().extrude(-200)