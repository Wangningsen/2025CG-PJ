import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-31,0))
r=w0.sketch().segment((-54,-15),(-25,-15)).arc((34,-96),(12,3)).segment((12,100)).segment((-54,100)).close().assemble().reset().face(w0.sketch().arc((-16,-15),(22,-90),(12,-7)).segment((12,-15)).close().assemble(),mode='s').finalize().extrude(54).union(w0.workplane(offset=62/2).moveTo(-37,42).cylinder(62,28))