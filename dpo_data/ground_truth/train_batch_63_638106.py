import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-7,-34),(7,-34)).segment((7,-17)).arc((18,0),(7,17)).segment((7,34)).segment((-7,34)).segment((-7,17)).arc((-18,0),(-7,-17)).close().assemble().finalize().extrude(200)