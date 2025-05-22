import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-56,-88),(56,-88)).segment((56,88)).segment((34,88)).arc((5,86),(-23,88)).segment((-56,88)).close().assemble().finalize().extrude(-200)