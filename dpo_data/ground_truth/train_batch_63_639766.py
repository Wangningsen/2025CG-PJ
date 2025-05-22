import cadquery as cq
w0=cq.Workplane('YZ',origin=(-76,0,0))
r=w0.sketch().segment((-87,-37),(85,-64)).segment((100,30)).segment((16,43)).segment((16,37)).segment((-76,37)).close().assemble().finalize().extrude(46).union(w0.sketch().segment((-54,-84),(11,-84)).segment((11,11)).segment((7,11)).arc((-73,76),(-54,-26)).close().assemble().finalize().extrude(152))