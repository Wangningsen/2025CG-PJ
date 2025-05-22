import cadquery as cq
w0=cq.Workplane('YZ',origin=(19,0,0))
w1=cq.Workplane('XY',origin=(0,0,-15))
r=w0.sketch().push([(0,-9)]).circle(69).circle(59,mode='s').rect(78,88).finalize().extrude(81).union(w1.sketch().segment((-100,-36),(-85,-36)).arc((-94,0),(-85,36)).segment((-100,36)).close().assemble().finalize().extrude(93))