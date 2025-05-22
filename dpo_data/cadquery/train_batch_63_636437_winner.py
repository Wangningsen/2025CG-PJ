import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-27))
w1=cq.Workplane('XY',origin=(0,0,-6))
r=w0.sketch().arc((11,-71),(46,-83),(82,-71)).close().assemble().reset().face(w0.sketch().segment((11,14),(82,14)).arc((46,26),(11,14)).assemble()).reset().face(w0.sketch().arc((85,-66),(100,-24),(85,17)).close().assemble()).finalize().extrude(-16).union(w1.sketch().segment((-100,-77),(23,-77)).segment((23,-20)).arc((55,68),(-32,35)).segment((-100,35)).close().assemble().finalize().extrude(49))