import cadquery as cq
w0=cq.Workplane('YZ',origin=(-5,0,0))
w1=cq.Workplane('YZ',origin=(-20,0,0))
r=w0.sketch().push([(-32,-45)]).circle(41).push([(18,32)]).circle(47).finalize().extrude(-39).union(w0.workplane(offset=-20/2).moveTo(59,69).cylinder(20,7)).union(w0.workplane(offset=33/2).moveTo(-74,0).cylinder(33,26)).union(w1.sketch().segment((36,-52),(52,-52)).segment((52,-16)).arc((98,6),(75,51)).arc((49,86),(41,44)).arc((29,18),(40,-9)).segment((36,-9)).close().assemble().push([(65,17)]).rect(26,34,mode='s').finalize().extrude(64))