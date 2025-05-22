import cadquery as cq
w0=cq.Workplane('YZ',origin=(32,0,0))
w1=cq.Workplane('ZX',origin=(0,-7,0))
r=w0.sketch().segment((-49,6),(-25,-25)).segment((-19,-20)).arc((-36,-9),(-43,11)).close().assemble().reset().face(w0.sketch().arc((-3,42),(15,30),(21,11)).segment((27,16)).segment((3,47)).close().assemble()).finalize().extrude(68).union(w1.sketch().segment((-44,-100),(-30,-100)).segment((-30,-75)).arc((-26,-66),(-30,-58)).segment((-30,-33)).segment((-44,-33)).segment((-44,-58)).arc((-47,-66),(-44,-75)).close().assemble().finalize().extrude(56))