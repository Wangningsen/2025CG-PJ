import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,50,0))
w1=cq.Workplane('YZ',origin=(16,0,0))
r=w0.sketch().segment((-100,-10),(-87,-10)).arc((-9,-81),(43,10)).segment((43,75)).segment((-40,75)).segment((-40,50)).arc((-69,31),(-85,0)).segment((-85,8)).segment((-89,8)).segment((-89,-5)).segment((-100,-5)).close().assemble().push([(-45,-54)]).circle(9,mode='s').finalize().extrude(-99).union(w1.sketch().segment((0,87),(21,87)).arc((13,93),(21,100)).segment((0,100)).close().assemble().finalize().extrude(66))