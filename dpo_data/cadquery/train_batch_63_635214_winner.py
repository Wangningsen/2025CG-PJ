import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,8))
r=w0.sketch().segment((-90,88),(-67,58)).segment((-52,69)).segment((-75,100)).close().assemble().reset().face(w0.sketch().segment((-5,-69),(44,-100)).segment((90,-28)).segment((85,-24)).segment((85,18)).segment((8,18)).segment((8,-37)).segment((16,-37)).close().assemble()).finalize().extrude(-16)