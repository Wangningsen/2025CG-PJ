import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
r=w0.workplane(offset=-64/2).moveTo(-62,26).box(76,56,64).union(w0.sketch().push([(52,-6)]).circle(48).push([(67,24)]).circle(2,mode='s').push([(82,42.5)]).rect(22,7).finalize().extrude(22))