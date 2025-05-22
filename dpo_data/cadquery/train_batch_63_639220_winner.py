import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().arc((-69,4),(24,-44),(63,49)).segment((63,4)).close().assemble().finalize().extrude(-200)