import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-20,0))
w1=cq.Workplane('ZX',origin=(0,-6,0))
r=w0.sketch().segment((51,-4),(54,-2)).segment((51,2)).close().assemble().finalize().extrude(-19).union(w0.sketch().segment((81,-100),(82,-99)).segment((81,-97)).close().assemble().finalize().extrude(82)).union(w1.sketch().segment((-82,56),(-69,56)).arc((-61,11),(-16,3)).arc((51,30),(-7,66)).arc((-25,77),(-44,77)).segment((-44,100)).segment((-82,100)).close().assemble().finalize().extrude(-56))