import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-68,-35),(0,-32),(68,-44)).segment((68,44)).segment((-68,44)).close().assemble().finalize().extrude(-200)