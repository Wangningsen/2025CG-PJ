import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.workplane(offset=-200/2).moveTo(0,4).cylinder(200,95).union(w0.sketch().push([(22,-44)]).circle(55).push([(39.5,-30)]).rect(15,42,mode='s').finalize().extrude(-112))