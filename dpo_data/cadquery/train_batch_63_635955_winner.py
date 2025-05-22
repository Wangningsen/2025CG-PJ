import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
r=w0.sketch().segment((-89,-65),(-7,-65)).arc((100,-4),(-7,58)).segment((-7,76)).segment((-89,76)).segment((-89,39)).arc((-100,6),(-89,-27)).close().assemble().reset().face(w0.sketch().segment((-88,8),(-83,-12)).segment((-10,3)).segment((-14,23)).segment((-17,23)).segment((-17,29)).close().assemble(),mode='s').finalize().extrude(-30)