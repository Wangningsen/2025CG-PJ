import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-98,44),(-70,44)).arc((73,-63),(-46,73)).segment((-67,73)).arc((-83,75),(-98,79)).close().assemble().finalize().extrude(-200)