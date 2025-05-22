import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
r=w0.sketch().segment((63,-82),(63,-62)).segment((92,-62)).arc((9,9),(69,-84)).segment((69,-82)).close().assemble().finalize().extrude(93).union(w0.workplane(offset=118/2).moveTo(-84,74).cylinder(118,16))