import cadquery as cq
w0=cq.Workplane('YZ',origin=(-74,0,0))
r=w0.sketch().segment((-100,47),(-84,41)).arc((-91,-27),(-35,-74)).segment((-35,-96)).segment((-6,-96)).segment((-6,-74)).arc((24,-61),(46,-37)).arc((96,43),(6,71)).arc((1,73),(-6,74)).segment((-6,96)).segment((-35,96)).segment((-35,74)).arc((-58,66),(-77,50)).segment((-96,58)).close().assemble().finalize().extrude(148)