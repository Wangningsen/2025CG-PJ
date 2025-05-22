import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-22,0))
w1=cq.Workplane('ZX',origin=(0,-6,0))
r=w0.workplane(offset=-19/2).moveTo(51.5,-0.5).box(5,5,19).union(w0.sketch().segment((81,-100),(82,-99)).segment((81,-97)).close().assemble().finalize().extrude(84)).union(w1.sketch().segment((-82,56),(-69,56)).arc((-62,12),(-18,4)).arc((50,22),(-6,66)).arc((-23,76),(-44,77)).segment((-44,100)).segment((-82,100)).close().assemble().finalize().extrude(-56))