import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-68))
r=w0.sketch().segment((-93,55),(-61,1)).segment((8,42)).arc((91,11),(12,50)).segment((-17,100)).close().assemble().finalize().extrude(55).union(w0.sketch().segment((33,-99),(41,-100)).segment((45,-71)).arc((47,3),(37,-70)).close().assemble().finalize().extrude(137))