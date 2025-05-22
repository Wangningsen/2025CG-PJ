import cadquery as cq
w0=cq.Workplane('YZ',origin=(-79,0,0))
r=w0.sketch().segment((-22,-100),(-13,-100)).segment((-13,0)).arc((22,15),(-13,33)).segment((-13,100)).segment((-22,100)).close().assemble().reset().face(w0.sketch().segment((-13,8),(-1,0)).segment((16,23)).segment((3,33)).segment((-13,13)).close().assemble(),mode='s').finalize().extrude(158)