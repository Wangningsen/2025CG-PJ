import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
w1=cq.Workplane('XY',origin=(0,0,0))
r=w0.workplane(offset=-70/2).moveTo(68,60.5).box(6,79,70).union(w0.sketch().arc((42,-66),(45,-75),(43,-86)).arc((45,-88),(48,-89)).segment((56,-74)).close().assemble().finalize().extrude(-3)).union(w0.workplane(offset=56/2).moveTo(3,-78).cylinder(56,22)).union(w1.sketch().push([(-77.5,14)]).rect(45,36).push([(-78,13)]).circle(6,mode='s').finalize().extrude(-71))