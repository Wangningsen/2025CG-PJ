import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-58,-4),(57,-13)).segment((58,3)).segment((-58,13)).segment((-58,10)).arc((-54,2),(-58,-4)).assemble().finalize().extrude(-200)