import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-12,0))
w1=cq.Workplane('YZ',origin=(-28,0,0))
r=w0.sketch().segment((-41,-37),(36,-44)).segment((41,4)).segment((-36,12)).close().assemble().finalize().extrude(-88).union(w0.workplane(offset=19/2).moveTo(0,-16).cylinder(19,54)).union(w0.sketch().segment((-51,-25),(-35,-25)).arc((-10,-39),(15,-25)).segment((51,-25)).segment((51,-8)).segment((19,-8)).arc((-10,19),(-38,-8)).segment((-51,-8)).close().assemble().finalize().extrude(112)).union(w1.workplane(offset=97/2).moveTo(-22,-39).box(4,24,97))