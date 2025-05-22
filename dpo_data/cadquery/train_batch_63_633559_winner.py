import cadquery as cq
w0=cq.Workplane('YZ',origin=(25,0,0))
r=w0.sketch().push([(8,-71)]).rect(20,58).rect(20,16,mode='s').finalize().extrude(-83).union(w0.workplane(offset=33/2).moveTo(0,68).box(70,64,33))