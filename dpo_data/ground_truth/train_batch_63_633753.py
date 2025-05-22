import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.workplane(offset=126/2).cylinder(126,88).union(w0.sketch().segment((-8,-63),(8,-63)).segment((8,-8)).arc((11,0),(8,8)).segment((8,63)).segment((-8,63)).segment((-8,8)).arc((-11,0),(-8,-8)).close().assemble().finalize().extrude(200))