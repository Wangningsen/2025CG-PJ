import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-1))
r=w0.workplane(offset=-16/2).moveTo(-67,26).cylinder(16,33).union(w0.sketch().push([(-7,42)]).circle(29).push([(53,-24)]).circle(47).finalize().extrude(18))