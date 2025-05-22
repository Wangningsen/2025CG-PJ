import cadquery as cq
w0=cq.Workplane('YZ',origin=(46,0,0))
w1=cq.Workplane('XY',origin=(0,0,-68))
r=w0.workplane(offset=-138/2).moveTo(-46.5,-46).box(51,108,138).union(w1.sketch().arc((25,39),(65,28),(91,0)).segment((91,72)).segment((25,72)).close().assemble().finalize().extrude(168))