import cadquery as cq
w0=cq.Workplane('YZ',origin=(49,0,0))
r=w0.sketch().arc((-96,-39),(96,-11),(-87,55)).segment((-92,4)).segment((-88,3)).segment((-93,-12)).segment((-94,-12)).close().assemble().finalize().extrude(-99)