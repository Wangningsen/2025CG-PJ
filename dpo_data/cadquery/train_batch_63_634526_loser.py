import cadquery as cq
w0=cq.Workplane('YZ',origin=(-80,0,0))
w1=cq.Workplane('YZ',origin=(-58,0,0))
r=w0.workplane(offset=104/2).moveTo(-34.5,64).box(23,72,104).union(w0.workplane(offset=162/2).moveTo(-34,64).box(52,22,162)).union(w1.sketch().arc((-43,-49),(47,-82),(-1,-2)).arc((-14,-28),(-43,-49)).assemble().finalize().extrude(-24))