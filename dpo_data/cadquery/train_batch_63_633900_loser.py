import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,96))
r=w0.sketch().segment((-100,10),(-58,10)).arc((94,-30),(-40,51)).arc((-44,47),(-49,49)).segment((-49,59)).segment((-100,59)).close().assemble().finalize().extrude(-192)