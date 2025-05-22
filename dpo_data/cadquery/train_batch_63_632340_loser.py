import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
w1=cq.Workplane('ZX',origin=(0,33,0))
r=w0.workplane(offset=-17/2).moveTo(-16,24.5).box(94,65,17).union(w0.sketch().push([(76,-56)]).circle(24).circle(13,mode='s').finalize().extrude(-16)).union(w0.workplane(offset=48/2).moveTo(-44,77).cylinder(48,2)).union(w1.sketch().segment((-56,-67),(-19,-67)).arc((54,-74),(-13,-43)).segment((-13,-57)).segment((-56,-57)).close().assemble().push([(15,-33)]).rect(4,8,mode='s').finalize().extrude(-29))