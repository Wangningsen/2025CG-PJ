import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,23))
r=w0.sketch().push([(-82,-3.5)]).rect(36,93).reset().face(w0.sketch().arc((84,49),(57,10),(99,32)).arc((96,35),(98,35)).arc((94,42),(88,47)).arc((86,46),(84,49)).assemble()).reset().face(w0.sketch().segment((60,21),(67,12)).segment((98,35)).segment((91,44)).close().assemble(),mode='s').finalize().extrude(-46)