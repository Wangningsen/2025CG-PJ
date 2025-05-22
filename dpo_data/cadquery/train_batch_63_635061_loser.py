import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
r=w0.sketch().arc((-24,-78),(-21,-65),(-24,-52)).close().assemble().finalize().extrude(-114).union(w0.sketch().arc((2,36),(4,46),(14,39)).arc((-4,77),(2,36)).assemble().push([(-7,48)]).circle(6,mode='s').finalize().extrude(86))