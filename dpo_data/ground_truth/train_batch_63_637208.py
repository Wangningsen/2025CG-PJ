import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.sketch().segment((-100,-70),(100,-70)).segment((100,59)).segment((-59,59)).segment((-59,57)).segment((-61,57)).segment((-61,59)).segment((-100,59)).close().assemble().finalize().extrude(-19).union(w0.sketch().arc((-17,25),(22,22),(32,-16)).segment((69,29)).segment((19,70)).close().assemble().finalize().extrude(45))