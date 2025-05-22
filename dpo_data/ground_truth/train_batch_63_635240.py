import cadquery as cq
w0=cq.Workplane('YZ',origin=(24,0,0))
r=w0.workplane(offset=-124/2).moveTo(-70,-60).cylinder(124,3).union(w0.sketch().push([(-70,-60)]).circle(5).push([(33,51)]).rect(84,28).finalize().extrude(76))