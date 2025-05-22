import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-61,0))
r=w0.sketch().segment((-93,-48),(-18,-48)).segment((-18,-7)).arc((21,74),(-69,77)).segment((-93,77)).close().assemble().finalize().extrude(50).union(w0.sketch().segment((10,-90),(72,-100)).segment((93,20)).segment((31,31)).close().assemble().push([(57,-6)]).circle(11,mode='s').finalize().extrude(121))