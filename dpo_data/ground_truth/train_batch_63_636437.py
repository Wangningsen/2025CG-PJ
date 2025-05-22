import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-43))
w1=cq.Workplane('XY',origin=(0,0,-6))
r=w0.sketch().arc((11,-70),(45,-82),(81,-70)).close().assemble().reset().face(w0.sketch().segment((11,15),(81,15)).arc((45,27),(11,15)).assemble()).reset().face(w0.sketch().arc((85,-66),(100,-28),(85,11)).segment((85,-6)).segment((87,-6)).segment((87,-49)).segment((85,-49)).close().assemble()).finalize().extrude(16).union(w1.sketch().segment((-100,-76),(23,-76)).segment((23,-19)).arc((55,68),(-32,35)).segment((-100,35)).close().assemble().finalize().extrude(49))