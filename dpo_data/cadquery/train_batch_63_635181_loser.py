import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-61))
w1=cq.Workplane('ZX',origin=(0,-11,0))
r=w0.sketch().segment((10,-88),(18,-100)).segment((33,-89)).arc((55,-88),(64,-66)).segment((76,-54)).segment((69,-44)).segment((60,-49)).arc((41,-47),(28,-63)).arc((48,-67),(62,-81)).segment((35,-44)).arc((34,-45),(33,-45)).arc((31,-53),(25,-60)).arc((25,-62),(24,-65)).close().assemble().finalize().extrude(40).union(w0.workplane(offset=157/2).moveTo(-2,26).cylinder(157,74)).union(w1.workplane(offset=75/2).moveTo(-78,-26).box(36,14,75))