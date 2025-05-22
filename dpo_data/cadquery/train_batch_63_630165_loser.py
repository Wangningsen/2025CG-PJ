import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
r=w0.sketch().arc((-93,-37),(-61,-58),(-45,-90)).arc((75,66),(-93,-37)).assemble().finalize().extrude(68)