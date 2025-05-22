import cadquery as cq
w0=cq.Workplane('YZ',origin=(-31,0,0))
w1=cq.Workplane('YZ',origin=(-30,0,0))
r=w0.sketch().segment((-77,29),(-40,29)).segment((-40,21)).segment((-12,21)).segment((-12,29)).segment((23,29)).segment((23,93)).segment((-12,93)).segment((-12,100)).segment((-40,100)).segment((-40,93)).segment((-77,93)).close().assemble().finalize().extrude(-13).union(w0.workplane(offset=75/2).moveTo(24.5,-67.5).box(105,63,75)).union(w1.workplane(offset=71/2).moveTo(24.5,-67.5).box(41,65,71))