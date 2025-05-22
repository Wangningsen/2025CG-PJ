import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
w1=cq.Workplane('XY',origin=(0,0,49))
r=w0.sketch().push([(-9,5)]).circle(26).circle(13,mode='s').push([(65,65)]).circle(35).finalize().extrude(-89).union(w0.sketch().push([(-92.5,-69)]).rect(15,62).push([(3,-31)]).circle(34).finalize().extrude(-39)).union(w1.sketch().segment((-32,-28),(14,-28)).segment((14,-11)).arc((42,56),(-25,39)).segment((-32,39)).close().assemble().finalize().extrude(26))