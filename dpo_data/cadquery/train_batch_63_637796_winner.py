import cadquery as cq
w0=cq.Workplane('YZ',origin=(-44,0,0))
w1=cq.Workplane('YZ',origin=(-45,0,0))
r=w0.workplane(offset=16/2).moveTo(-1,-48).cylinder(16,11).union(w0.sketch().segment((-55,19),(6,-19)).segment((19,4)).arc((33,20),(40,40)).segment((55,63)).segment((-6,100)).segment((-19,77)).arc((-33,63),(-40,43)).close().assemble().push([(26,-73)]).circle(27).circle(5,mode='s').finalize().extrude(88)).union(w1.sketch().arc((-11,-48),(11,-52),(-11,-46)).arc((-10,-47),(-11,-48)).assemble().finalize().extrude(81))