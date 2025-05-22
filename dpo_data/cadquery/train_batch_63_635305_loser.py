import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-70,40),(-68,40)).segment((-68,45)).arc((-69,46),(-68,47)).segment((-68,57)).segment((-70,57)).close().assemble().reset().face(w0.sketch().segment((-4,0),(41,-57)).segment((70,-34)).segment((25,23)).arc((12,8),(-4,0)).assemble()).finalize().extrude(-200)