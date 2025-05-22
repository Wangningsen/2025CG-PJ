import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,49))
r=w0.workplane(offset=-98/2).moveTo(-56.5,-73).box(23,54,98).union(w0.sketch().segment((-85,7),(-8,-33)).segment((19,23)).arc((82,21),(28,69)).segment((-35,100)).close().assemble().push([(-23,34)]).circle(6,mode='s').finalize().extrude(-82))