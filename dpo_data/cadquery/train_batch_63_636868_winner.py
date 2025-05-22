import cadquery as cq
w0=cq.Workplane('YZ',origin=(-40,0,0))
r=w0.sketch().segment((-52,-81),(100,-81)).segment((100,-43)).arc((24,-79),(-52,-43)).close().assemble().finalize().extrude(36).union(w0.sketch().segment((-100,1),(-57,-17)).arc((-41,-27),(-23,-31)).segment((20,-48)).segment((52,33)).segment((10,50)).arc((-7,60),(-25,64)).segment((-68,81)).close().assemble().finalize().extrude(80))