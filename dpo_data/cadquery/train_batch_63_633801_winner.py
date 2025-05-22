import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-20,0))
w1=cq.Workplane('YZ',origin=(58,0,0))
r=w0.sketch().segment((20,-100),(54,-100)).segment((20,-41)).close().assemble().reset().face(w0.sketch().segment((58,-41),(91,-100)).segment((91,-41)).close().assemble()).finalize().extrude(17).union(w0.workplane(offset=86/2).moveTo(-57,-47).cylinder(86,1)).union(w1.sketch().push([(-28.5,-50.5)]).rect(75,81).rect(71,43,mode='s').finalize().extrude(42))