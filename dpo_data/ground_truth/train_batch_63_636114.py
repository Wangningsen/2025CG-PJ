import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((43,45),(56,58)).arc((-51,-63),(58,56)).segment((45,43)).close().assemble().finalize().extrude(-200).union(w0.sketch().push([(3,-3)]).rect(16,72).circle(8,mode='s').finalize().extrude(-118))