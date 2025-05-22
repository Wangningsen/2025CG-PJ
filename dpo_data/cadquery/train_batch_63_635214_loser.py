import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-8))
r=w0.sketch().segment((-90,88),(-66,58)).segment((-52,69)).segment((-75,100)).close().assemble().reset().face(w0.sketch().segment((-6,-70),(44,-100)).segment((90,-28)).segment((84,-24)).segment((85,-24)).segment((85,18)).segment((8,18)).segment((8,-35)).segment((18,-35)).close().assemble()).finalize().extrude(16)