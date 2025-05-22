import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().segment((-100,-91),(0,-91)).segment((0,-67)).segment((100,-67)).segment((100,-46)).segment((0,-46)).segment((0,-27)).segment((-66,-6)).segment((-57,32)).segment((12,5)).arc((27,72),(-46,73)).segment((-48,74)).segment((-54,57)).segment((-100,56)).close().assemble().finalize().extrude(24)