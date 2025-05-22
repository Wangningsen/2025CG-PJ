import cadquery as cq
w0=cq.Workplane('YZ',origin=(-53,0,0))
w1=cq.Workplane('YZ',origin=(-44,0,0))
r=w0.sketch().segment((34,9),(53,9)).arc((43,13),(34,9)).assemble().finalize().extrude(-12).union(w0.sketch().segment((-100,-46),(9,-46)).arc((99,11),(-6,29)).arc((2,22),(8,14)).segment((-100,14)).close().assemble().finalize().extrude(46)).union(w1.sketch().push([(43,0)]).circle(5).rect(4,8,mode='s').finalize().extrude(109))