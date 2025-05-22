import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-17))
r=w0.sketch().segment((-67,-6),(8,-6)).segment((8,69)).segment((-1,69)).segment((-1,100)).arc((20,-98),(-31,95)).segment((-31,69)).segment((-67,69)).close().assemble().finalize().extrude(34)