import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,23,0))
w1=cq.Workplane('XY',origin=(0,0,-23))
r=w0.sketch().arc((33,23),(42,23),(39,31)).arc((-37,81),(33,23)).assemble().push([(0,54)]).circle(26,mode='s').push([(38,26)]).circle(2,mode='s').finalize().extrude(21).union(w1.sketch().segment((-77,-47),(-73,-47)).segment((-73,-25)).arc((-50,0),(-73,25)).segment((-73,47)).segment((-77,47)).segment((-77,25)).arc((-100,0),(-77,-25)).close().assemble().push([(-75,0)]).circle(25,mode='s').finalize().extrude(59))