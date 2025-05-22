import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-58,-46),(58,-46)).segment((58,46)).segment((-58,23)).close().assemble().finalize().extrude(-200)