import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
w1=cq.Workplane('ZX',origin=(0,6,0))
r=w0.sketch().segment((27,-96),(34,-100)).segment((36,-98)).segment((29,-94)).close().assemble().finalize().extrude(-69).union(w0.workplane(offset=-35/2).moveTo(-37,85).cylinder(35,15)).union(w1.sketch().segment((38,-9),(42,-9)).arc((44,-16),(52,-22)).segment((52,5)).arc((44,0),(42,-8)).segment((38,-8)).close().assemble().finalize().extrude(55))