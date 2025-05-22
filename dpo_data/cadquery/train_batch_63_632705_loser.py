import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-58))
w1=cq.Workplane('XY',origin=(0,0,-100))
r=w0.workplane(offset=104/2).moveTo(-47,-14).cylinder(104,22).union(w0.sketch().segment((-8,-7),(36,-7)).arc((14,-1),(-8,-7)).assemble().finalize().extrude(158)).union(w1.sketch().arc((-51,-43),(-31,-46),(-27,-63)).arc((39,56),(-51,-43)).assemble().finalize().extrude(29))