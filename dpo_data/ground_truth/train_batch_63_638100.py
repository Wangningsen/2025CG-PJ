import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,59))
r=w0.sketch().segment((-100,-56),(-1,-56)).segment((31,-50)).segment((32,-56)).segment((100,-56)).segment((100,56)).segment((-100,56)).close().assemble().finalize().extrude(-118)