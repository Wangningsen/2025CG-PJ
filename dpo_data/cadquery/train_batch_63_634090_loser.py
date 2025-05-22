import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,53))
r=w0.sketch().segment((-70,-11),(-66,-18)).segment((20,46)).segment((16,53)).close().assemble().push([(81,69)]).circle(19).finalize().extrude(-106).union(w0.workplane(offset=-44/2).moveTo(-85,-73).cylinder(44,15))