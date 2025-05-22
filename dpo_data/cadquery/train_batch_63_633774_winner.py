import cadquery as cq
w0=cq.Workplane('YZ',origin=(-69,0,0))
w1=cq.Workplane('XY',origin=(0,0,-5))
r=w0.sketch().arc((-21,-47),(11,-65),(5,-29)).arc((-74,57),(-21,-47)).assemble().finalize().extrude(-8).union(w0.workplane(offset=81/2).moveTo(-40,8).cylinder(81,4)).union(w1.workplane(offset=55/2).moveTo(71,94).cylinder(55,6))