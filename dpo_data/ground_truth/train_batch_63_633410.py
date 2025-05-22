import cadquery as cq
w0=cq.Workplane('YZ',origin=(-13,0,0))
r=w0.sketch().segment((-66,18),(-36,18)).arc((30,-93),(-21,26)).segment((-21,100)).segment((-66,100)).close().assemble().push([(0.5,-35.5)]).rect(69,85,mode='s').finalize().extrude(26)