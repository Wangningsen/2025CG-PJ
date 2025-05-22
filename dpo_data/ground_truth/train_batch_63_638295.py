import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().circle(95).reset().face(w0.sketch().segment((-78,14),(-38,-3)).arc((-15,-35),(24,-30)).segment((64,-47)).segment((78,-14)).segment((38,3)).arc((15,35),(-24,30)).segment((-64,47)).close().assemble(),mode='s').finalize().extrude(200)