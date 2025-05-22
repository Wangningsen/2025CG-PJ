import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,17,0))
r=w0.workplane(offset=-61/2).moveTo(-6,-27).cylinder(61,37).union(w0.sketch().segment((-51,-57),(-50,-57)).arc((17,-96),(37,-19)).segment((37,8)).segment((-18,8)).arc((-49,99),(-51,2)).close().assemble().push([(-40,50)]).circle(32,mode='s').finalize().extrude(-57)).union(w0.workplane(offset=27/2).moveTo(84,32).box(10,76,27))