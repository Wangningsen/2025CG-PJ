import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
r=w0.sketch().segment((-100,-56),(-1,-56)).segment((32,-51)).segment((33,-56)).segment((100,-56)).segment((100,56)).segment((-100,56)).close().assemble().finalize().extrude(118)