import cadquery as cq
w0=cq.Workplane('YZ',origin=(13,0,0))
r=w0.sketch().segment((-67,18),(-36,18)).arc((24,-96),(-21,25)).segment((-21,100)).segment((-67,100)).close().assemble().push([(0,-36)]).rect(70,84,mode='s').finalize().extrude(-26)