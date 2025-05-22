import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
r=w0.sketch().segment((-79,-48),(-6,-94)).segment((4,-100)).segment((11,-90)).segment((5,-82)).segment((79,-2)).segment((70,6)).segment((79,20)).segment((43,43)).segment((59,72)).segment((10,100)).segment((-11,62)).segment((-5,54)).segment((-79,-26)).segment((-70,-35)).close().assemble().finalize().extrude(-17)