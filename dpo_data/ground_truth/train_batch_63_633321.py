import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
r=w0.sketch().segment((-100,-30),(-58,-64)).segment((1,8)).segment((65,8)).segment((65,56)).segment((-14,56)).segment((-24,64)).segment((-30,56)).segment((-52,56)).segment((-52,29)).close().assemble().finalize().extrude(-2).union(w0.sketch().push([(82,7)]).circle(18).circle(17,mode='s').finalize().extrude(78))