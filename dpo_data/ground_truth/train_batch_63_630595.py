import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,54))
r=w0.sketch().push([(-46.5,-23)]).rect(107,4).push([(57,0)]).circle(43).finalize().extrude(-112).union(w0.workplane(offset=4/2).moveTo(-47,-23).cylinder(4,19))