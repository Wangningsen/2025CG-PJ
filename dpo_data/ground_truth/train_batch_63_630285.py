import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-57))
r=w0.sketch().segment((-98,29),(-55,-43)).arc((-47,-71),(-27,-91)).segment((-21,-100)).segment((-15,-96)).arc((36,-91),(64,-49)).segment((98,-29)).segment((21,100)).close().assemble().finalize().extrude(-22).union(w0.workplane(offset=137/2).cylinder(137,55))