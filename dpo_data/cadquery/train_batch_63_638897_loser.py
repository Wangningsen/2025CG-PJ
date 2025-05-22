import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-53,14),(50,-22),(-49,23)).arc((-37,12),(-53,14)).assemble().finalize().extrude(-200)