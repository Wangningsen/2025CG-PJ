import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-84,37),(15,-91)).segment((84,-37)).segment((-15,91)).close().assemble().finalize().extrude(200)