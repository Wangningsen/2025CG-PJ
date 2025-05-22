import cadquery as cq
w0=cq.Workplane('YZ',origin=(45,0,0))
w1=cq.Workplane('XY',origin=(0,0,-68))
r=w0.workplane(offset=-137/2).moveTo(-46.5,-46).box(51,108,137).union(w0.sketch().segment((1,-46),(20,-73)).segment((61,-45)).segment((43,-18)).close().assemble().finalize().extrude(7)).union(w1.sketch().arc((25,39),(63,29),(91,1)).segment((91,72)).segment((25,72)).close().assemble().finalize().extrude(168))