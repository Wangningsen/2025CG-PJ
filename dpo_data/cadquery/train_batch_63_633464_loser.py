import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-52,0))
r=w0.workplane(offset=63/2).moveTo(-23,-8).cylinder(63,57).union(w0.sketch().arc((-70,-21),(-13,-100),(29,-14)).segment((29,-6)).segment((39,-6)).segment((39,30)).arc((80,56),(39,82)).segment((39,100)).segment((-70,100)).close().assemble().push([(-61,-8)]).circle(3,mode='s').finalize().extrude(104))