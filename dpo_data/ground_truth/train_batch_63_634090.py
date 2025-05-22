import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,52))
r=w0.sketch().segment((-70,-11),(-65,-17)).segment((20,47)).segment((16,53)).close().assemble().push([(81,69)]).circle(19).finalize().extrude(-105).union(w0.workplane(offset=-43/2).moveTo(-85,-72).cylinder(43,15))