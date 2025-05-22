import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.sketch().arc((-93,-38),(-62,-56),(-47,-88)).arc((76,65),(-93,-38)).assemble().finalize().extrude(-68)