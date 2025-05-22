import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
w1=cq.Workplane('YZ',origin=(-21,0,0))
r=w0.sketch().push([(24,0)]).circle(76).reset().face(w0.sketch().segment((-53,11),(-4,-70)).segment((75,-11)).segment((26,70)).close().assemble(),mode='s').finalize().extrude(-23).union(w0.sketch().segment((-100,-55),(-79,-55)).arc((-48,-69),(-17,-55)).segment((4,-55)).segment((4,-29)).arc((11,58),(-77,33)).arc((-86,17),(-88,-4)).segment((-100,-4)).close().assemble().finalize().extrude(50)).union(w1.workplane(offset=66/2).moveTo(-48,18).cylinder(66,19))