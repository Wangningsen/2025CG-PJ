import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
r=w0.sketch().push([(-36.5,-49)]).rect(81,102).reset().face(w0.sketch().arc((37,38),(38,42),(41,45)).segment((41,48)).segment((46,48)).arc((53,49),(61,48)).segment((66,48)).segment((66,45)).arc((39,99),(37,38)).assemble()).push([(45.5,68.5)]).rect(23,23,mode='s').finalize().extrude(-13)