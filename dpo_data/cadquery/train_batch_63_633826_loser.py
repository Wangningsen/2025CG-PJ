import cadquery as cq
w0=cq.Workplane('YZ',origin=(-69,0,0))
r=w0.workplane(offset=8/2).moveTo(0,-14).cylinder(8,86).union(w0.sketch().push([(-43,83)]).rect(38,34).rect(10,12,mode='s').finalize().extrude(138))