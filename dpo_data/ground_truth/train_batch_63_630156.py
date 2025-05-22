import cadquery as cq
w0=cq.Workplane('YZ',origin=(12,0,0))
w1=cq.Workplane('ZX',origin=(0,19,0))
r=w0.sketch().push([(-80.5,9.5)]).rect(39,119).reset().face(w0.sketch().segment((-92,0),(-70,0)).segment((-70,7)).segment((-70,12)).segment((-70,18)).segment((-92,18)).segment((-92,12)).segment((-92,7)).close().assemble(),mode='s').finalize().extrude(59).union(w1.sketch().segment((-69,-71),(-50,-71)).segment((-50,-66)).arc((-61,-67),(-69,-66)).close().assemble().finalize().extrude(81))