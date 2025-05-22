import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
w1=cq.Workplane('ZX',origin=(0,6,0))
r=w0.sketch().segment((27,-96),(34,-100)).segment((36,-98)).segment((29,-94)).segment((28,-96)).close().assemble().finalize().extrude(-68).union(w0.workplane(offset=-34/2).moveTo(-37,85).cylinder(34,15)).union(w1.sketch().segment((38,-9),(43,-9)).arc((45,-17),(52,-22)).segment((52,5)).arc((45,0),(43,-8)).segment((38,-8)).close().assemble().finalize().extrude(55))