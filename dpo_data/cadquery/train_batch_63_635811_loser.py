import cadquery as cq
w0=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.sketch().segment((-46,12),(100,12)).segment((100,56)).segment((30,56)).segment((30,55)).segment((28,55)).segment((28,56)).segment((-46,56)).close().assemble().push([(52,33)]).circle(2,mode='s').finalize().extrude(8).union(w0.workplane(offset=58/2).moveTo(-69,-25).cylinder(58,31))