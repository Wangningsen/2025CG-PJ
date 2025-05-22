import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,0))
r=w0.sketch().segment((-59,-34),(-19,-34)).arc((0,-41),(19,-34)).segment((50,-34)).segment((50,-9)).arc((59,13),(50,34)).segment((-59,34)).close().assemble().finalize().extrude(-100).union(w0.workplane(offset=100/2).moveTo(-4,0).cylinder(100,46))