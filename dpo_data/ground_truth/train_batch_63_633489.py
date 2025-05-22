import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,56))
r=w0.workplane(offset=-113/2).moveTo(55.5,21).box(89,130,113).union(w0.sketch().arc((-72,-83),(-71,-80),(-68,-79)).arc((-93,-55),(-72,-83)).assemble().finalize().extrude(-31))