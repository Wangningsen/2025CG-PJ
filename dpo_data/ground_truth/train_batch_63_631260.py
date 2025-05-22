import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,96))
r=w0.sketch().circle(100).reset().face(w0.sketch().segment((-40,-83),(-40,-77)).arc((-41,-80),(-40,-83)).assemble(),mode='s').reset().face(w0.sketch().arc((-40,-84),(-27,-94),(-13,-84)).close().assemble(),mode='s').push([(-1.5,79)]).rect(13,4,mode='s').finalize().extrude(-192)