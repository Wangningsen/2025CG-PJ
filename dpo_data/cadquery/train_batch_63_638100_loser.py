import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
r=w0.sketch().segment((-100,-56),(0,-56)).segment((34,-49)).segment((35,-56)).segment((100,-56)).segment((100,56)).segment((-100,56)).close().assemble().finalize().extrude(118)