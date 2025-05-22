import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,27))
w1=cq.Workplane('XY',origin=(0,0,6))
r=w0.sketch().segment((-27,0),(-15,0)).arc((0,-2),(15,0)).segment((27,0)).segment((27,6)).arc((51,49),(27,92)).segment((27,98)).segment((15,98)).arc((0,100),(-15,98)).segment((-27,98)).segment((-27,92)).arc((-51,49),(-27,6)).close().assemble().push([(-19.5,42)]).rect(43,60,mode='s').push([(28,-99)]).circle(1).finalize().extrude(-16).union(w1.sketch().push([(30.5,-70.5)]).rect(25,21).push([(31,-71)]).circle(6,mode='s').finalize().extrude(-33))