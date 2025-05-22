import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
r=w0.sketch().segment((75,-91),(100,-91)).segment((100,-51)).arc((88,-52),(76,-48)).segment((76,-21)).segment((75,-21)).close().assemble().finalize().extrude(23).union(w0.sketch().segment((-5,64),(-5,84)).arc((-71,-31),(17,68)).segment((17,64)).close().assemble().finalize().extrude(46))