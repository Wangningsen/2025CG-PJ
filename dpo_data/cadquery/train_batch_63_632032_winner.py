import cadquery as cq
w0=cq.Workplane('YZ',origin=(33,0,0))
w1=cq.Workplane('YZ',origin=(-33,0,0))
r=w0.workplane(offset=-67/2).cylinder(67,100).union(w1.sketch().segment((-49,-57),(38,-57)).segment((38,-77)).segment((49,-77)).segment((49,-57)).segment((83,-57)).segment((83,-33)).segment((49,-33)).segment((49,-23)).segment((38,-23)).segment((38,-33)).segment((-49,-33)).close().assemble().finalize().extrude(17))