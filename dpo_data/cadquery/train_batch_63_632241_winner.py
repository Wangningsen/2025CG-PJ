import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,19))
w1=cq.Workplane('XY',origin=(0,0,-4))
r=w0.sketch().segment((-40,-89),(46,-89)).arc((88,-84),(54,-55)).segment((54,-3)).arc((54,97),(-12,29)).segment((-40,29)).close().assemble().finalize().extrude(-51).union(w1.sketch().arc((-90,-19),(-28,-17),(-58,30)).arc((-66,0),(-90,-19)).assemble().finalize().extrude(37))