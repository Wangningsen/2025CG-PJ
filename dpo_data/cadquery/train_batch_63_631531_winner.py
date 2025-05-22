import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-18))
r=w0.sketch().segment((-100,-39),(-95,-46)).segment((-45,-12)).segment((-49,-5)).close().assemble().reset().face(w0.sketch().segment((41,29),(59,-14)).segment((100,4)).segment((82,46)).close().assemble()).finalize().extrude(36)