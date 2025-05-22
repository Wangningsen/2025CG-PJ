import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
r=w0.sketch().push([(30,73)]).circle(3).reset().face(w0.sketch().segment((29,70),(31,75)).segment((29,71)).close().assemble(),mode='s').finalize().extrude(-71).union(w0.sketch().push([(-20,63)]).circle(37).push([(28,-71)]).circle(29).finalize().extrude(19))