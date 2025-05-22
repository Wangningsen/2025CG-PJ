import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,17,0))
r=w0.workplane(offset=-61/2).moveTo(-7,-27.5).box(78,71,61).union(w0.sketch().arc((-51,-35),(8,-99),(37,-17)).segment((37,7)).segment((-16,7)).arc((-49,99),(-51,2)).close().assemble().push([(-41,50)]).circle(31,mode='s').finalize().extrude(-57)).union(w0.workplane(offset=27/2).moveTo(83.5,32).box(11,74,27))