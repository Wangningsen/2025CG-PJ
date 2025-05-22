import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-71))
r=w0.sketch().push([(-72,61)]).circle(28).push([(22,-11)]).circle(78).reset().face(w0.sketch().segment((-32,1),(-30,-29)).segment((-2,-28)).arc((24,-40),(48,-24)).segment((76,-22)).segment((74,8)).segment((46,6)).arc((20,19),(-4,3)).close().assemble(),mode='s').finalize().extrude(142)