import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
w1=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().segment((-100,-76),(23,-76)).segment((23,-18)).arc((56,66),(-32,35)).segment((-100,35)).close().assemble().finalize().extrude(49).union(w1.sketch().push([(55,-27)]).circle(45).reset().face(w1.sketch().segment((12,-31),(17,-31)).arc((55,-72),(92,-31)).segment((97,-31)).segment((97,-21)).segment((92,-21)).arc((55,18),(17,-21)).segment((12,-21)).close().assemble(),mode='s').finalize().extrude(16))