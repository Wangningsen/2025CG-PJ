import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-71))
r=w0.sketch().push([(-72,61)]).circle(28).push([(22,-11)]).circle(78).reset().face(w0.sketch().segment((-32,0),(-29,-30)).segment((0,-27)).arc((21,-40),(44,-25)).segment((76,-22)).segment((73,8)).segment((43,6)).arc((22,19),(0,4)).close().assemble(),mode='s').finalize().extrude(142)