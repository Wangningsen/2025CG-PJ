import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-58))
w1=cq.Workplane('XY',origin=(0,0,-71))
r=w0.workplane(offset=104/2).moveTo(-47,-14).cylinder(104,22).union(w0.sketch().segment((-8,-7),(36,-7)).arc((14,-1),(-8,-7)).assemble().finalize().extrude(158)).union(w1.sketch().arc((-50,-44),(-34,-45),(-26,-62)).arc((37,57),(-50,-44)).assemble().finalize().extrude(-29))