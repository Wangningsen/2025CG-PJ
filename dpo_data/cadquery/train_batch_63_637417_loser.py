import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
w1=cq.Workplane('YZ',origin=(26,0,0))
r=w0.sketch().push([(-20,63)]).circle(37).push([(28,-71)]).circle(29).finalize().extrude(19).union(w1.workplane(offset=-71/2).moveTo(30,73).box(4,6,71))