import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-22,0))
r=w0.workplane(offset=-5/2).moveTo(22,71).cylinder(5,29).union(w0.sketch().segment((-63,-75),(17,-100)).segment((20,-95)).arc((59,-33),(-16,-23)).segment((-44,-14)).close().assemble().push([(58,-48)]).circle(3,mode='s').finalize().extrude(49))