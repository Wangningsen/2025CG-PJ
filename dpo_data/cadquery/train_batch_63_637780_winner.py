import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
w1=cq.Workplane('XY',origin=(0,0,49))
r=w0.sketch().push([(-9,5)]).circle(26).circle(13,mode='s').push([(65,65)]).circle(35).finalize().extrude(-89).union(w0.sketch().push([(-92.5,-69)]).rect(15,62).reset().face(w0.sketch().segment((10,-64),(16,-64)).segment((16,-62)).arc((-17,-5),(10,-64)).assemble()).finalize().extrude(-39)).union(w1.sketch().segment((-32,-28),(14,-28)).segment((14,-9)).arc((48,49),(-18,39)).segment((-32,39)).close().assemble().finalize().extrude(26))