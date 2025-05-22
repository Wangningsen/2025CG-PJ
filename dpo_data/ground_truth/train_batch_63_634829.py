import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,34,0))
w1=cq.Workplane('XY',origin=(0,0,-36))
r=w0.sketch().push([(-7,35)]).circle(58).rect(84,70,mode='s').finalize().extrude(-90).union(w0.sketch().push([(63.5,32)]).rect(73,86).reset().face(w0.sketch().segment((50,55),(64,59)).segment((64,61)).segment((50,57)).close().assemble(),mode='s').finalize().extrude(-85)).union(w0.workplane(offset=-79/2).moveTo(81,-83).cylinder(79,10)).union(w1.workplane(offset=-64/2).moveTo(34.5,0).box(99,140,64))