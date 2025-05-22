import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
r=w0.sketch().segment((-100,-30),(-57,-64)).segment((-1,8)).segment((66,8)).segment((66,56)).segment((-15,56)).segment((-21,64)).segment((-29,56)).segment((-52,56)).segment((-52,28)).close().assemble().finalize().extrude(-2).union(w0.sketch().push([(82,7)]).circle(18).circle(17,mode='s').finalize().extrude(78))