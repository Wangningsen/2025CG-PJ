import cadquery as cq
w0=cq.Workplane('YZ',origin=(40,0,0))
w1=cq.Workplane('YZ',origin=(90,0,0))
r=w0.sketch().segment((-100,-20),(-31,-70)).segment((3,-25)).segment((6,-27)).segment((6,-29)).segment((100,-29)).segment((100,70)).segment((6,70)).segment((6,35)).segment((-36,66)).close().assemble().finalize().extrude(-130).union(w1.sketch().segment((34,-58),(43,-58)).segment((43,-59)).segment((59,-59)).segment((59,-58)).segment((65,-58)).segment((65,13)).segment((59,13)).segment((59,14)).segment((43,14)).segment((43,13)).segment((34,13)).close().assemble().finalize().extrude(-117))