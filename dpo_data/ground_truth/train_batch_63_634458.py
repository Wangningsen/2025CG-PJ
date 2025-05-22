import cadquery as cq
w0=cq.Workplane('YZ',origin=(-20,0,0))
w1=cq.Workplane('YZ',origin=(11,0,0))
r=w0.workplane(offset=-80/2).moveTo(-8,-8).cylinder(80,17).union(w0.sketch().segment((-58,-25),(-43,-47)).segment((-18,-31)).arc((-8,-33),(1,-31)).arc((45,46),(-31,0)).arc((-32,-4),(-32,-9)).close().assemble().finalize().extrude(120)).union(w1.sketch().arc((-30,37),(3,-58),(-7,42)).arc((-18,37),(-30,37)).assemble().finalize().extrude(-42))