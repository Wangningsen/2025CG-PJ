import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-36))
r=w0.workplane(offset=61/2).moveTo(5.5,56).box(29,80,61).union(w0.sketch().push([(-58,-54)]).circle(42).circle(36,mode='s').push([(27,-52)]).rect(42,20).push([(58,36)]).circle(42).finalize().extrude(72))