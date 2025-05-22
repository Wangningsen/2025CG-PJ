import cadquery as cq
w0=cq.Workplane('YZ',origin=(-55,0,0))
w1=cq.Workplane('ZX',origin=(0,53,0))
r=w0.workplane(offset=4/2).moveTo(15,0).cylinder(4,85).union(w0.sketch().arc((-33,-5),(-46,-80),(15,-32)).segment((64,-47)).segment((70,-27)).arc((99,-11),(87,18)).segment((94,57)).segment((-6,83)).close().assemble().push([(37.5,-6.5)]).rect(63,25,mode='s').finalize().extrude(119)).union(w1.workplane(offset=-99/2).moveTo(55,-32).cylinder(99,32))