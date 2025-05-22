import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,23,0))
w1=cq.Workplane('XY',origin=(0,0,36))
r=w0.sketch().arc((33,22),(44,26),(40,36)).arc((-38,80),(33,22)).assemble().reset().face(w0.sketch().arc((22,38),(22,40),(23,42)).arc((-24,64),(22,38)).assemble(),mode='s').finalize().extrude(21).union(w1.sketch().segment((-77,-47),(-73,-47)).segment((-73,-25)).arc((-50,0),(-73,25)).segment((-73,47)).segment((-77,47)).segment((-77,25)).arc((-100,0),(-77,-25)).close().assemble().push([(-75,0)]).circle(25,mode='s').finalize().extrude(-59))