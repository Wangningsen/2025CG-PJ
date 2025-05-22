import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,19,0))
w1=cq.Workplane('XY',origin=(0,0,36))
r=w0.sketch().push([(0,-21.5)]).rect(10,25).push([(0,-22)]).circle(1,mode='s').finalize().extrude(-94).union(w0.sketch().segment((-64,46),(-28,0)).arc((-29,-44),(12,-57)).segment((48,-100)).segment((64,-87)).segment((28,-43)).arc((29,2),(-12,15)).segment((-48,58)).close().assemble().finalize().extrude(20)).union(w1.workplane(offset=-19/2).moveTo(24,0).cylinder(19,76))