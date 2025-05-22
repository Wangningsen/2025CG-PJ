import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-33))
r=w0.workplane(offset=-5/2).cylinder(5,100).union(w0.sketch().arc((-64,-27),(-34,-60),(12,-68)).segment((0,-52)).arc((46,-25),(44,27)).segment((64,27)).arc((34,60),(-12,68)).segment((0,52)).arc((-46,25),(-44,-27)).close().assemble().finalize().extrude(71))