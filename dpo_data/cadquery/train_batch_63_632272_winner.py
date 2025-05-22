import cadquery as cq
w0=cq.Workplane('YZ',origin=(-83,0,0))
r=w0.workplane(offset=147/2).moveTo(80.5,33.5).box(39,25,147).union(w0.sketch().push([(-57,-3)]).circle(43).push([(-78,12)]).rect(20,32,mode='s').finalize().extrude(167))