import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-70))
r=w0.sketch().segment((-27,-75),(23,-100)).segment((54,-40)).segment((35,-30)).segment((22,13)).arc((-19,98),(-8,4)).segment((-25,-4)).segment((-13,-44)).close().assemble().finalize().extrude(139)