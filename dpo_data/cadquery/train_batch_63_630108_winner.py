import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,61))
r=w0.sketch().push([(-77,17)]).circle(23).push([(52,0)]).circle(48).push([(30,-10)]).rect(4,6,mode='s').reset().face(w0.sketch().segment((36,-13),(40,-13)).arc((58,-30),(79,-13)).segment((88,-13)).segment((88,-7)).segment((78,-7)).arc((58,10),(37,-7)).segment((36,-7)).close().assemble(),mode='s').finalize().extrude(-122)