import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
r=w0.sketch().arc((-24,-78),(-21,-65),(-24,-52)).close().assemble().finalize().extrude(-114).union(w0.sketch().segment((-12,46),(-7,54)).segment((14,39)).arc((-2,77),(2,36)).close().assemble().finalize().extrude(86))