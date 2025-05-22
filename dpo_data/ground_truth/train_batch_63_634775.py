import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-94,0))
r=w0.sketch().segment((-58,-93),(45,-100)).segment((58,83)).segment((34,85)).arc((3,100),(-30,89)).segment((-45,90)).close().assemble().reset().face(w0.sketch().arc((-32,22),(-33,-31),(19,-42)).arc((22,-42),(23,-39)).arc((41,-10),(32,22)).arc((0,9),(-32,22)).assemble(),mode='s').finalize().extrude(189)