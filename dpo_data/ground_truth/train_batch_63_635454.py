import cadquery as cq
w0=cq.Workplane('YZ',origin=(32,0,0))
w1=cq.Workplane('ZX',origin=(0,-7,0))
r=w0.sketch().segment((-49,6),(-25,-25)).segment((-19,-20)).arc((-36,-9),(-43,11)).close().assemble().reset().face(w0.sketch().arc((-3,42),(14,31),(21,11)).segment((27,16)).segment((3,47)).close().assemble()).finalize().extrude(68).union(w1.sketch().segment((-44,-100),(-30,-100)).segment((-30,-74)).arc((-26,-67),(-30,-59)).segment((-30,-33)).segment((-44,-33)).segment((-44,-59)).arc((-47,-67),(-44,-74)).close().assemble().finalize().extrude(56))