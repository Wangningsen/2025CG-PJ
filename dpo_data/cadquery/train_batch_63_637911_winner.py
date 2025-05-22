import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
r=w0.sketch().segment((-62,-74),(8,-74)).segment((8,-100)).segment((62,-100)).segment((62,-1)).segment((37,-1)).arc((-11,98),(8,-12)).segment((8,-26)).segment((-62,-26)).close().assemble().finalize().extrude(82)