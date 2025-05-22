import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
w1=cq.Workplane('XY',origin=(0,0,-24))
r=w0.sketch().arc((-76,-19),(-93,-77),(-32,-77)).arc((-62,-55),(-76,-19)).assemble().push([(-82,-54.5)]).rect(20,1,mode='s').push([(59,51)]).circle(41).finalize().extrude(20).union(w0.sketch().segment((9,2),(33,2)).segment((33,7)).segment((15,7)).segment((15,6)).segment((13,6)).segment((13,7)).segment((9,7)).close().assemble().finalize().extrude(39)).union(w1.workplane(offset=-27/2).moveTo(66,1).cylinder(27,23))