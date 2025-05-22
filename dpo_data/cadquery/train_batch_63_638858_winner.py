import cadquery as cq
w0=cq.Workplane('YZ',origin=(23,0,0))
w1=cq.Workplane('YZ',origin=(3,0,0))
r=w0.sketch().push([(-45,0.5)]).rect(60,53).push([(43,-68)]).circle(32).finalize().extrude(-99).union(w0.sketch().segment((-67,32),(-37,32)).segment((-37,21)).segment((-26,21)).segment((-26,32)).segment((3,32)).segment((3,90)).segment((-26,90)).segment((-26,100)).segment((-37,100)).segment((-37,90)).segment((-67,90)).close().assemble().finalize().extrude(53)).union(w1.sketch().segment((-50,-15),(-40,-15)).segment((-40,15)).arc((-45,14),(-50,15)).close().assemble().finalize().extrude(40))