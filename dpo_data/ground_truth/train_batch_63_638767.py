import cadquery as cq
w0=cq.Workplane('YZ',origin=(19,0,0))
r=w0.sketch().segment((-92,-45),(22,-100)).segment((37,-70)).arc((38,-60),(45,-52)).segment((92,45)).segment((-22,100)).close().assemble().finalize().extrude(-95).union(w0.workplane(offset=56/2).box(18,46,56))