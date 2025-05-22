import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-91,15),(43,15)).segment((-41,81)).close().assemble().reset().face(w0.sketch().segment((47,-81),(91,-22)).segment((47,13)).close().assemble()).finalize().extrude(200)