import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-12))
w1=cq.Workplane('XY',origin=(0,0,-33))
r=w0.sketch().push([(-57,-33)]).circle(25).rect(40,20,mode='s').finalize().extrude(-88).union(w0.sketch().push([(60,36)]).circle(22).reset().face(w0.sketch().segment((50,28),(63,22)).segment((69,36)).segment((55,41)).close().assemble(),mode='s').finalize().extrude(63)).union(w1.sketch().push([(60,36)]).circle(21).rect(22,30,mode='s').finalize().extrude(133))