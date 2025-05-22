import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-52,0))
r=w0.workplane(offset=57/2).moveTo(-48,-5).cylinder(57,32).union(w0.sketch().segment((-70,-6),(-55,-6)).arc((-18,-100),(20,-6)).segment((39,-6)).segment((39,30)).arc((80,56),(39,82)).segment((39,100)).segment((-70,100)).close().assemble().finalize().extrude(104))