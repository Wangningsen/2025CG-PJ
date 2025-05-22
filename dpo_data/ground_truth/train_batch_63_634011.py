import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-36))
r=w0.sketch().push([(5.5,56)]).rect(29,80).push([(18,46)]).circle(1,mode='s').finalize().extrude(61).union(w0.sketch().push([(-58,-54)]).circle(42).circle(36,mode='s').push([(27,-52)]).rect(42,20).push([(57,36)]).circle(43).finalize().extrude(72))