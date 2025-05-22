import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
r=w0.sketch().segment((63,-84),(63,-62)).segment((93,-62)).arc((8,8),(70,-84)).close().assemble().finalize().extrude(93).union(w0.workplane(offset=118/2).moveTo(-84,74).cylinder(118,16))