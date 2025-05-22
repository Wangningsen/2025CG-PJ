import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
r=w0.workplane(offset=-59/2).moveTo(3,0).cylinder(59,13).union(w0.sketch().arc((-42,-60),(-31,-62),(-23,-71)).arc((33,-68),(72,-28)).arc((56,6),(64,43)).arc((-50,54),(-42,-60)).assemble().finalize().extrude(141))