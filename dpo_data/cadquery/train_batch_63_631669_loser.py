import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-33,-15),(1,-15)).arc((4,-13),(8,-15)).segment((33,-15)).segment((33,15)).arc((2,-5),(-33,9)).close().assemble().finalize().extrude(200)