import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,11))
w1=cq.Workplane('XY',origin=(0,0,-26))
r=w0.sketch().segment((-27,0),(-11,0)).arc((0,-2),(11,0)).segment((27,0)).segment((27,6)).arc((51,49),(27,92)).segment((27,98)).segment((11,98)).arc((0,100),(-11,98)).segment((-27,98)).segment((-27,92)).arc((-51,49),(-27,6)).close().assemble().push([(-19.5,42)]).rect(43,60,mode='s').push([(29,-99)]).circle(1).finalize().extrude(16).union(w1.sketch().push([(30.5,-70.5)]).rect(25,21).push([(31,-71)]).circle(6,mode='s').push([(38.5,-64)]).rect(3,6,mode='s').finalize().extrude(32))