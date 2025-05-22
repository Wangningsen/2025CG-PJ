import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().push([(31.5,-12)]).rect(65,126).rect(25,10,mode='s').finalize().extrude(15).union(w0.sketch().arc((-64,34),(-14,37),(31,15)).segment((34,18)).segment((-14,75)).close().assemble().finalize().extrude(200))