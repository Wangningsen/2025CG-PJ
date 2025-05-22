import cadquery as cq
w0=cq.Workplane('YZ',origin=(19,0,0))
r=w0.sketch().push([(-6.5,64.5)]).rect(79,59).push([(6,-43.5)]).rect(80,113).push([(27,-87)]).rect(12,4,mode='s').finalize().extrude(-99).union(w0.workplane(offset=61/2).moveTo(-6.5,64.5).box(75,71,61))