import cadquery as cq
w0=cq.Workplane('YZ',origin=(0,0,0))
w1=cq.Workplane('YZ',origin=(9,0,0))
r=w0.sketch().push([(-46,68)]).circle(32).push([(-21,-82)]).circle(18).reset().face(w0.sketch().segment((3,4),(5,-27)).segment((23,-26)).arc((29,-28),(34,-25)).segment((48,-24)).segment((46,7)).close().assemble()).finalize().extrude(-67).union(w1.sketch().segment((47,-13),(67,-13)).segment((67,5)).arc((78,24),(67,43)).segment((67,61)).segment((47,61)).segment((47,43)).arc((36,24),(47,5)).close().assemble().push([(57,24)]).circle(13,mode='s').finalize().extrude(58))