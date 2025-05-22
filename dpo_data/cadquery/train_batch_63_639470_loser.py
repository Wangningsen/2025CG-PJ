import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-12,0))
w1=cq.Workplane('ZX',origin=(0,-18,0))
r=w0.sketch().segment((-100,-48),(-17,-48)).segment((-17,28)).segment((-24,28)).arc((-34,33),(-44,28)).segment((-100,28)).close().assemble().finalize().extrude(-12).union(w1.sketch().segment((10,7),(39,7)).segment((39,-13)).segment((68,-13)).segment((68,7)).segment((97,7)).segment((97,16)).segment((100,16)).segment((100,34)).segment((84,34)).segment((84,28)).segment((68,28)).segment((68,48)).segment((39,48)).segment((39,28)).segment((10,28)).close().assemble().finalize().extrude(42))