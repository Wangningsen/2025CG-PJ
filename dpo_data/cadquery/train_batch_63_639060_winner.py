import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,71))
r=w0.sketch().segment((-51,-91),(9,-91)).segment((9,58)).segment((3,58)).arc((-88,79),(-51,-6)).close().assemble().push([(65,-63)]).circle(35).finalize().extrude(-142)