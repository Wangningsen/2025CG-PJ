import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-20,0))
w1=cq.Workplane('YZ',origin=(58,0,0))
r=w0.sketch().segment((20,-100),(53,-100)).segment((53,-98)).segment((22,-42)).segment((24,-41)).segment((20,-41)).close().assemble().reset().face(w0.sketch().segment((58,-43),(88,-99)).segment((86,-100)).segment((91,-100)).segment((91,-41)).segment((58,-41)).close().assemble()).finalize().extrude(18).union(w0.workplane(offset=86/2).moveTo(-57,-47).cylinder(86,1)).union(w1.sketch().push([(-28,-50.5)]).rect(74,81).rect(70,43,mode='s').finalize().extrude(42))