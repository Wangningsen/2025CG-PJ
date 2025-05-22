import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,17,0))
w1=cq.Workplane('XY',origin=(0,0,-45))
r=w0.workplane(offset=-117/2).moveTo(-16,38).cylinder(117,52).union(w1.sketch().arc((-90,-24),(-33,-11),(6,-53)).segment((19,-53)).segment((19,-33)).arc((43,-11),(72,1)).segment((72,8)).segment((19,8)).segment((19,100)).segment((-90,100)).close().assemble().finalize().extrude(113))