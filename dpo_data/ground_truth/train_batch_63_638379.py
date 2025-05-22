import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.sketch().segment((-31,-2),(-27,-20)).segment((14,-12)).segment((10,6)).close().assemble().finalize().extrude(-75).union(w0.sketch().segment((-72,-18),(72,-18)).segment((72,-12)).segment((-72,20)).close().assemble().finalize().extrude(125))