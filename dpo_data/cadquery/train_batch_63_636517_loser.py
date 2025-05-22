import cadquery as cq
w0=cq.Workplane('YZ',origin=(-76,0,0))
r=w0.sketch().segment((91,-4),(100,-4)).segment((100,55)).segment((91,55)).segment((91,15)).arc((93,14),(91,13)).close().assemble().finalize().extrude(104).union(w0.workplane(offset=152/2).moveTo(-16,-49.5).box(168,11,152))