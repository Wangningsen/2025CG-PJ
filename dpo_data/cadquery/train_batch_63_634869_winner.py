import cadquery as cq
w0=cq.Workplane('YZ',origin=(30,0,0))
r=w0.sketch().rect(152,200).rect(98,130,mode='s').finalize().extrude(-69).union(w0.sketch().segment((3,-10),(6,-10)).segment((6,-1)).arc((4,0),(6,1)).segment((6,10)).segment((3,10)).close().assemble().finalize().extrude(9))