import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-28))
w1=cq.Workplane('XY',origin=(0,0,-24))
r=w0.sketch().segment((-64,-22),(57,-74)).segment((100,28)).segment((86,34)).arc((79,38),(71,40)).segment((-22,79)).close().assemble().finalize().extrude(117).union(w1.workplane(offset=-65/2).moveTo(-29.5,-30.5).box(141,97,65))