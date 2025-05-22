import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
r=w0.sketch().segment((-100,-91),(0,-91)).segment((0,-67)).segment((100,-67)).segment((100,-46)).segment((0,-46)).segment((0,-27)).segment((-70,-4)).segment((-60,28)).segment((12,5)).arc((18,81),(-54,56)).segment((-100,56)).close().assemble().finalize().extrude(-24)