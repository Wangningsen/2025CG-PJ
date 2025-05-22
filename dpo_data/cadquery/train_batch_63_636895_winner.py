import cadquery as cq
w0=cq.Workplane('YZ',origin=(-16,0,0))
r=w0.workplane(offset=-84/2).moveTo(51,-55).cylinder(84,39).union(w0.sketch().segment((-90,-4),(-67,-4)).arc((-49,-22),(-31,-4)).segment((12,-4)).segment((12,94)).segment((-90,94)).close().assemble().push([(-39,44)]).circle(35,mode='s').finalize().extrude(116))