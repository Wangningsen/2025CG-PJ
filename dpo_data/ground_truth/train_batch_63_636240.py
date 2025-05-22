import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-21))
r=w0.sketch().segment((-15,31),(-11,58)).segment((61,48)).arc((-59,75),(-9,-38)).segment((-9,-100)).segment((75,-100)).segment((75,-37)).segment((4,-37)).arc((43,-18),(62,20)).close().assemble().finalize().extrude(41)