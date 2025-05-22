import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
r=w0.sketch().push([(31.5,-30.5)]).rect(47,77).push([(40,-39)]).circle(4,mode='s').finalize().extrude(-79).union(w0.sketch().push([(-56,25)]).circle(44).push([(60.5,-36.5)]).rect(11,65).push([(94.5,-35)]).rect(11,62).finalize().extrude(47))