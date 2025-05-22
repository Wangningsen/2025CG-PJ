import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,3,0))
r=w0.sketch().push([(-96,46)]).circle(4).reset().face(w0.sketch().segment((-19,-17),(15,-34)).segment((40,15)).segment((40,-5)).segment((74,-5)).segment((74,18)).segment((43,18)).segment((51,36)).segment((16,55)).close().assemble()).finalize().extrude(-27).union(w0.workplane(offset=22/2).moveTo(59,-14).cylinder(22,41))