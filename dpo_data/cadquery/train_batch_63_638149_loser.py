import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,3,0))
r=w0.sketch().push([(-96,45)]).circle(4).reset().face(w0.sketch().segment((-20,-16),(14,-34)).segment((34,3)).segment((40,3)).segment((40,11)).segment((38,11)).segment((51,36)).segment((16,55)).close().assemble()).push([(56.5,6.5)]).rect(35,23).finalize().extrude(-27).union(w0.workplane(offset=21/2).moveTo(59,-14).cylinder(21,41))