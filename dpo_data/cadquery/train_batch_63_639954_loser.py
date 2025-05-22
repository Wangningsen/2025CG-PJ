import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,71))
r=w0.sketch().push([(-72,61)]).circle(28).push([(22,-11)]).circle(78).reset().face(w0.sketch().segment((-32,1),(-29,-30)).segment((-11,-28)).arc((18,-40),(45,-25)).segment((76,-22)).segment((74,8)).segment((48,6)).arc((19,19),(-8,3)).close().assemble(),mode='s').finalize().extrude(-142)