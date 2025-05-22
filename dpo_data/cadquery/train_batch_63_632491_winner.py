import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-24,0))
w1=cq.Workplane('XY',origin=(0,0,-27))
r=w0.sketch().segment((-22,-9),(27,-9)).segment((27,49)).segment((9,49)).arc((1,39),(-7,49)).segment((-22,49)).close().assemble().finalize().extrude(-76).union(w1.sketch().segment((-49,52),(-29,52)).segment((-29,41)).segment((-9,41)).segment((-9,52)).segment((11,52)).segment((11,71)).segment((-9,71)).segment((-9,73)).arc((-16,84),(-20,100)).segment((-29,100)).segment((-29,89)).segment((-49,89)).close().assemble().finalize().extrude(15))