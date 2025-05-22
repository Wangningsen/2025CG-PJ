import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-49))
w1=cq.Workplane('YZ',origin=(21,0,0))
r=w0.sketch().segment((-27,93),(-26,77)).arc((-33,48),(-19,23)).segment((-17,7)).segment((38,14)).segment((36,30)).arc((43,59),(29,84)).segment((27,100)).close().assemble().reset().face(w0.sketch().arc((35,50),(35,59),(38,68)).arc((32,59),(35,50)).assemble(),mode='s').finalize().extrude(3).union(w1.sketch().segment((-92,8),(-91,8)).segment((-91,38)).segment((-57,38)).arc((-92,43),(-92,8)).assemble().finalize().extrude(-65))