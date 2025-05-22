import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,5,0))
w1=cq.Workplane('YZ',origin=(0,0,0))
r=w0.sketch().push([(-42,3)]).circle(8).push([(-42,2.5)]).rect(10,7,mode='s').push([(46.5,76.5)]).rect(59,47).finalize().extrude(-51).union(w0.sketch().push([(-57,-12)]).circle(13).circle(8,mode='s').finalize().extrude(-37)).union(w1.workplane(offset=-100/2).moveTo(26,-57).cylinder(100,20))