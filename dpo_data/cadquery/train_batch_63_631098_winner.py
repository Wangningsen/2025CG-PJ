import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
w1=cq.Workplane('XY',origin=(0,0,10))
r=w0.sketch().segment((24,4),(50,4)).arc((37,20),(24,4)).assemble().finalize().extrude(-87).union(w0.sketch().segment((-11,43),(-10,-8)).segment((10,-8)).segment((10,-10)).segment((11,-10)).arc((25,-22),(43,-21)).segment((85,-20)).segment((82,47)).close().assemble().finalize().extrude(-64)).union(w1.sketch().segment((-85,-11),(-82,-11)).arc((-33,-49),(15,-11)).segment((18,-11)).segment((18,11)).segment((15,11)).arc((-33,49),(-82,11)).segment((-85,11)).close().assemble().finalize().extrude(90))