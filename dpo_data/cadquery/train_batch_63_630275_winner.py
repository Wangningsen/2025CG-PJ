import cadquery as cq
w0=cq.Workplane('YZ',origin=(-2,0,0))
r=w0.sketch().push([(20,69)]).circle(14).push([(20,61)]).circle(4,mode='s').finalize().extrude(-98).union(w0.workplane(offset=102/2).moveTo(0,-34.5).box(70,97,102))