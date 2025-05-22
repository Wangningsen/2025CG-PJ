import cadquery as cq
w0=cq.Workplane('YZ',origin=(-31,0,0))
w1=cq.Workplane('YZ',origin=(-45,0,0))
r=w0.sketch().segment((-28,-99),(11,-99)).segment((11,-100)).segment((42,-100)).segment((42,-99)).segment((77,-99)).segment((77,-36)).segment((-28,-36)).close().assemble().finalize().extrude(75).union(w1.sketch().segment((-77,29),(-42,29)).segment((-42,22)).segment((-12,22)).segment((-12,29)).segment((23,29)).segment((23,93)).segment((-12,93)).segment((-12,100)).segment((-42,100)).segment((-42,93)).segment((-77,93)).close().assemble().finalize().extrude(14))