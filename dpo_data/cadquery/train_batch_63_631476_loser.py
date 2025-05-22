import cadquery as cq
w0=cq.Workplane('YZ',origin=(43,0,0))
r=w0.sketch().push([(-55,54.5)]).rect(90,43).push([(-45,46)]).circle(9,mode='s').reset().face(w0.sketch().segment((3,-72),(40,-72)).arc((52,-76),(65,-72)).segment((100,-72)).segment((100,-35)).segment((65,-35)).arc((52,-29),(40,-35)).segment((3,-35)).close().assemble()).finalize().extrude(-86)