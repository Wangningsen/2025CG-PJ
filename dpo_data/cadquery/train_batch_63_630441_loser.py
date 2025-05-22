import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,6,0))
w1=cq.Workplane('ZX',origin=(0,-1,0))
r=w0.sketch().segment((-2,-86),(9,-86)).segment((9,3)).segment((-2,3)).segment((-2,-54)).arc((-3,-60),(-2,-65)).close().assemble().push([(3,-76.5)]).rect(4,5,mode='s').push([(6.5,-46.5)]).rect(3,3,mode='s').finalize().extrude(-106).union(w0.sketch().segment((33,84),(44,70)).segment((44,90)).segment((33,90)).close().assemble().finalize().extrude(94)).union(w1.workplane(offset=-99/2).moveTo(0,-41).cylinder(99,49))