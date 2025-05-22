import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
w1=cq.Workplane('YZ',origin=(45,0,0))
r=w0.sketch().push([(30,73)]).circle(3).push([(30,72.5)]).rect(2,3,mode='s').finalize().extrude(-71).union(w1.sketch().push([(-20,63)]).circle(37).push([(28,-71)]).circle(29).finalize().extrude(-19))