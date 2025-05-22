import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,17,0))
w1=cq.Workplane('XY',origin=(0,0,-45))
r=w0.workplane(offset=-117/2).moveTo(-16,38).cylinder(117,52).union(w1.sketch().arc((-90,-24),(-50,-5),(-15,-33)).segment((19,-33)).segment((19,-13)).segment((42,-13)).arc((57,-8),(72,-7)).segment((72,8)).segment((19,8)).segment((19,100)).segment((-90,100)).close().assemble().finalize().extrude(113))