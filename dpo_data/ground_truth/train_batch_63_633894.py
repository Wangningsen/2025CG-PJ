import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,24))
w1=cq.Workplane('XY',origin=(0,0,9))
r=w0.sketch().push([(16,69)]).rect(70,44).push([(27,81)]).circle(4,mode='s').finalize().extrude(-31).union(w1.workplane(offset=-34/2).moveTo(-38,0).box(26,200,34))