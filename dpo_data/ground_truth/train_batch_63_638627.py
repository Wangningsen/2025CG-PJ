import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-65,-22),(65,-22)).arc((0,22),(-65,-22)).assemble().finalize().extrude(200)