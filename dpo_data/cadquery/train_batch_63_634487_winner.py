import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
r=w0.sketch().push([(-46.5,0)]).rect(95,200).push([(-47,0)]).circle(19,mode='s').finalize().extrude(-76).union(w0.sketch().push([(64,-21)]).circle(30).circle(8,mode='s').finalize().extrude(-6))